
from fastapi import FastAPI
from pydantic import BaseModel
import aiosqlite


app = FastAPI()


class SensorUpdate(BaseModel):
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


@app.put("/sensors/{sensor_id}")
async def update_sensor(
    sensor_id: int,
    sensor: SensorUpdate
):

    async with aiosqlite.connect(
        "factory.db"
    ) as db:

        await db.execute("""
        UPDATE sensors
        SET
        machine_id=?,
        temperature=?
        WHERE sensor_id=?
        """,
        (
            sensor.machine_id,
            sensor.temperature,
            sensor_id
        ))

        await db.commit()

        return {
            "message": "Updated"
        }