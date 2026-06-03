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


@app.get("/sensors")


async def get_sensors():

    async with aiosqlite.connect(
        "factory.db"
    ) as db:

        db.row_factory = aiosqlite.Row #what it does is it allows us to access the columns of the result set by name instead of by index. This makes our code more readable and easier to maintain.

        cursor = await db.execute("""
        SELECT *
        FROM sensors
        """)

        rows = await cursor.fetchall()

        return [
            dict(row) #what it does is it converts each row of the result set into a dictionary, where the keys are the column names and the values are the corresponding values for that row. This allows us to return the data in a more structured and easily consumable format.
            for row in rows
        ]