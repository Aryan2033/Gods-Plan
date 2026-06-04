import aiosqlite
from fastapi import FastAPI, Depends

DATABASE_URL = "factory.db" 


async def get_db():
    db = await aiosqlite.connect(DATABASE_URL)

    try:
        yield db
    finally:
        await db.close()

#what this code does is that it creates a dependency that can be injected into the route handlers. The get_db function is an asynchronous generator that connects to the database and yields the connection object. When the request is finished, the connection is closed.


