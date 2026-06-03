from fastapi import FastAPI
from pydantic import BaseModel
import aiosqlite


app = FastAPI()

class SensorCreate(BaseModel):
    machine_id: int
    temperature: float


@app.on_event("startup")
async def create_tables() -> None:
    async with aiosqlite.connect("factory.db") as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS sensors(
                sensor_id INTEGER PRIMARY KEY,
                machine_id INTEGER,
                temperature REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        await db.commit()


@app.post("/sensors")
async def create_sensor(sensor: SensorCreate):
    async with aiosqlite.connect("factory.db") as db:
        await db.execute(
            """
            INSERT INTO sensors (
                machine_id,
                temperature
            )
            VALUES (?, ?)
            """,
            (
                sensor.machine_id,
                sensor.temperature,
            ),
        )
        await db.commit()

    return {"message": "Sensor data created successfully"}

