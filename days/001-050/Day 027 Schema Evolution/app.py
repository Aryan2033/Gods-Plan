from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

DATABASE_URL = "sqlite+aiosqlite:///factory.db"

engine = create_async_engine(DATABASE_URL, echo=True)

SessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class Prediction(Base):

    __tablename__= "predictions"

    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    machine_id: Mapped[int] = mapped_column(nullable=False)
    prediction: Mapped[str] = mapped_column(nullable=False)

class PredictionCreate(BaseModel):
    machine_id: int
    prediction: str


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app= FastAPI(lifespan=lifespan)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/predictions")
async def create_prediction(
    prediction : PredictionCreate, db: AsyncSession = Depends(get_db)
):
    row = Prediction(
        machine_id=prediction.machine_id,
        prediction=prediction.prediction
                     )
    db.add(row)
    await db.commit()
    await db.refresh(row)
    return {"id": row.id, "machine_id": row.machine_id, "prediction": row.prediction}

@app.get("/predictions")
async def read_predictions(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Prediction))
    predictions = result.scalars().all()

    return [
        {"id": p.id, "machine_id": p.machine_id, "prediction": p.prediction}
        for p in predictions
    ]
