from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import engine, get_db
from models import Base, Machine, Prediction, SensorReading
from schemas import (
    MachineCreate,
    MachineRead,
    MachineUpdate,
    PredictionCreate,
    PredictionRead,
    SensorReadingCreate,
    SensorReadingRead,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(title="Day 28 Integration", lifespan=lifespan)


@app.get("/")
async def root():
    return {
        "message": "Day 28 integrates FastAPI, dependency injection, async SQLAlchemy, Pydantic validation, and Alembic-ready schema design."
    }


@app.get("/dashboard")
async def dashboard(db: AsyncSession = Depends(get_db)):
    machine_count = await db.scalar(select(func.count()).select_from(Machine))
    reading_count = await db.scalar(select(func.count()).select_from(SensorReading))
    prediction_count = await db.scalar(select(func.count()).select_from(Prediction))

    return {
        "machines": int(machine_count or 0),
        "sensor_readings": int(reading_count or 0),
        "predictions": int(prediction_count or 0),
    }


async def get_machine_or_404(db: AsyncSession, machine_id: int) -> Machine:
    machine = await db.get(Machine, machine_id)
    if machine is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Machine not found")
    return machine


@app.post("/machines", response_model=MachineRead, status_code=status.HTTP_201_CREATED)
async def create_machine(payload: MachineCreate, db: AsyncSession = Depends(get_db)):
    machine = Machine(
        name=payload.name,
        location=payload.location,
        owner_email=payload.owner_email,
    )
    db.add(machine)
    await db.commit()
    await db.refresh(machine)
    return machine


@app.get("/machines", response_model=list[MachineRead])
async def list_machines(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Machine).order_by(Machine.id))
    return list(result.all())


@app.get("/machines/{machine_id}", response_model=MachineRead)
async def read_machine(machine_id: int, db: AsyncSession = Depends(get_db)):
    return await get_machine_or_404(db, machine_id)


@app.patch("/machines/{machine_id}", response_model=MachineRead)
async def update_machine(
    machine_id: int,
    payload: MachineUpdate,
    db: AsyncSession = Depends(get_db),
):
    machine = await get_machine_or_404(db, machine_id)

    updates = payload.model_dump(exclude_unset=True)
    for field_name, field_value in updates.items():
        setattr(machine, field_name, field_value)

    await db.commit()
    await db.refresh(machine)
    return machine


@app.delete("/machines/{machine_id}")
async def delete_machine(machine_id: int, db: AsyncSession = Depends(get_db)):
    machine = await get_machine_or_404(db, machine_id)
    await db.delete(machine)
    await db.commit()
    return {"message": "Machine deleted"}


@app.post("/sensor-readings", response_model=SensorReadingRead, status_code=status.HTTP_201_CREATED)
async def create_sensor_reading(
    payload: SensorReadingCreate,
    db: AsyncSession = Depends(get_db),
):
    await get_machine_or_404(db, payload.machine_id)

    reading = SensorReading(
        machine_id=payload.machine_id,
        temperature=payload.temperature,
        humidity=payload.humidity,
        note=payload.note,
    )
    db.add(reading)
    await db.commit()
    await db.refresh(reading)
    return reading


@app.get("/sensor-readings", response_model=list[SensorReadingRead])
async def list_sensor_readings(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(SensorReading).order_by(SensorReading.id))
    return list(result.all())


@app.post("/predictions", response_model=PredictionRead, status_code=status.HTTP_201_CREATED)
async def create_prediction(
    payload: PredictionCreate,
    db: AsyncSession = Depends(get_db),
):
    await get_machine_or_404(db, payload.machine_id)

    prediction = Prediction(
        machine_id=payload.machine_id,
        prediction=payload.prediction,
        confidence_score=payload.confidence_score,
        model_version=payload.model_version,
        latency_ms=payload.latency_ms,
    )
    db.add(prediction)
    await db.commit()
    await db.refresh(prediction)
    return prediction


@app.get("/predictions", response_model=list[PredictionRead])
async def list_predictions(db: AsyncSession = Depends(get_db)):
    result = await db.scalars(select(Prediction).order_by(Prediction.id))
    return list(result.all())


@app.delete("/predictions/{prediction_id}")
async def delete_prediction(prediction_id: int, db: AsyncSession = Depends(get_db)):
    prediction = await db.get(Prediction, prediction_id)
    if prediction is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Prediction not found")

    await db.delete(prediction)
    await db.commit()
    return {"message": "Prediction deleted"}
