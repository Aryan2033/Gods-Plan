import asyncio
import aiosqlite

async def create_database():
    async with aiosqlite.connect('factory.db') as db:

        await db.execute("""
            CREATE TABLE IF NOT EXISTS schools (
                         student_id INTEGER PRIMARY KEY,
                         student_name TEXT,
                         location TEXT)""")
        
        await db.commit()

asyncio.run(create_database())

async def insert_data():
    async with aiosqlite.connect('factory.db') as db:
        await db.execute("""
            INSERT INTO schools (student_name, location) 
            VALUES (?,?)""", ("John Doe", "New York"))
        
        await db.commit()

async def get_data():
    async with aiosqlite.connect('factory.db') as db:
        cursor = await db.execute("SELECT * FROM schools")

        rows = await cursor.fetchall()
        for row in rows:  
            print(row) 
         #this approch for printing Useful for huge datasets.Why? Imagine:50 Million Rows fetchall(): Loads Everything Into RAM = crash. Iterating with fetchone(): Loads One Row at a Time = Memory Efficient.

asyncio.run(insert_data())
asyncio.run(get_data())




        

        