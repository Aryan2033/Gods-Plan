from fastapi import FastAPI, Depends

from DI import get_db

app = FastAPI()

@app.get("/machines")

async def get_machines(
    db: aiosqlite.Connection = Depends(get_db)  
    ):

    cursor = await db.execute("""
                              select * from machines
                              """)
    rows = await cursor.fetchall()

    return rows

