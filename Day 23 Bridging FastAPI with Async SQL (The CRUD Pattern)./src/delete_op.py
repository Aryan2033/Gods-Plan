from fastapi import FastAPI
import aiosqlite


app = FastAPI()


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


@app.delete("/sensors/{sensor_id}")
async def delete_sensor(
    sensor_id: int
):

    async with aiosqlite.connect(
        "factory.db"
    ) as db:

        await db.execute("""
        DELETE
        FROM sensors
        WHERE sensor_id=?
        """,
        (sensor_id,)
        )

        await db.commit()

        return {
            "message": "Deleted"
        }