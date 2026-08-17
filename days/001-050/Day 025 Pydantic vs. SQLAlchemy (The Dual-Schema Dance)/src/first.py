from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from sqlalchemy import select
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column
)

 
# DATABASE CONFIGURATION
 

DATABASE_URL = "sqlite+aiosqlite:///factory.db"

engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

 
# BASE CLASS
 

class Base(DeclarativeBase):
    pass

 
# SQLALCHEMY MODEL
 

class SensorLog(Base):

    __tablename__ = "sensor_logs"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    machine_id: Mapped[int]

    temperature: Mapped[float]

 
# PYDANTIC MODEL
 

class SensorCreate(BaseModel):

    machine_id: int
    temperature: float

 
# APPLICATION LIFESPAN
 

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting Application...")

    async with engine.begin() as conn:

        await conn.run_sync(
            Base.metadata.create_all
        )

    print("Database Ready")

    yield

    await engine.dispose()

    print("Application Shutdown")

 
# FASTAPI APP
 

app = FastAPI(
    lifespan=lifespan
)

 
# DATABASE DEPENDENCY
 

async def get_db():

    async with SessionLocal() as session:
        yield session

 
# CREATE SENSOR
 

@app.post("/sensors")
async def create_sensor(
    sensor: SensorCreate,
    db: AsyncSession = Depends(get_db)
):

    sensor_row = SensorLog(
        machine_id=sensor.machine_id,
        temperature=sensor.temperature
    )

    db.add(sensor_row)

    await db.commit()

    await db.refresh(sensor_row)

    return {
        "id": sensor_row.id,
        "machine_id": sensor_row.machine_id,
        "temperature": sensor_row.temperature
    }

 
# GET ALL SENSORS
 

@app.get("/sensors")
async def get_sensors(
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(SensorLog)
    )

    sensors = result.scalars().all()

    return [
        {
            "id": sensor.id,
            "machine_id": sensor.machine_id,
            "temperature": sensor.temperature
        }
        for sensor in sensors
    ]

 
# GET SINGLE SENSOR
 

@app.get("/sensors/{sensor_id}")
async def get_sensor(
    sensor_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(SensorLog).where(
            SensorLog.id == sensor_id
        )
    )

    sensor = result.scalar_one_or_none()

    if sensor is None:
        return {
            "message": "Sensor Not Found"
        }

    return {
        "id": sensor.id,
        "machine_id": sensor.machine_id,
        "temperature": sensor.temperature
    }

 
# UPDATE SENSOR
 

@app.put("/sensors/{sensor_id}")
async def update_sensor(
    sensor_id: int,
    sensor_data: SensorCreate,
    db: AsyncSession = Depends(get_db)   #what depends does is it allows us to inject the database session into our route handlers without having to manually create and manage the session in each handler. By using Depends(get_db), FastAPI will automatically call the get_db function to create a new database session for each request and pass it as an argument to the route handler. This helps to keep our code clean and ensures that we are properly managing our database connections.
):

    result = await db.execute(
        select(SensorLog).where(
            SensorLog.id == sensor_id
        )
    )

    sensor = result.scalar_one_or_none()

    if sensor is None:
        return {
            "message": "Sensor Not Found"
        }

    sensor.machine_id = sensor_data.machine_id
    sensor.temperature = sensor_data.temperature

    await db.commit()

    await db.refresh(sensor)

    return {
        "message": "Updated Successfully",
        "sensor": {
            "id": sensor.id,
            "machine_id": sensor.machine_id,
            "temperature": sensor.temperature
        }
    }

 
# DELETE SENSOR
 

@app.delete("/sensors/{sensor_id}")
async def delete_sensor(
    sensor_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(SensorLog).where(
            SensorLog.id == sensor_id
        )
    )

    sensor = result.scalar_one_or_none()

    if sensor is None:
        return {
            "message": "Sensor Not Found"
        }

    await db.delete(sensor)

    await db.commit()

    return {
        "message": "Deleted Successfully"
    }