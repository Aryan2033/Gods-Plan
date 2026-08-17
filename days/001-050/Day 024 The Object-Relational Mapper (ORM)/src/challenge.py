import asyncio
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from datetime import datetime, timezone
from pathlib import Path

# 1. Path setup matching our previous architecture
DB_PATH = Path("data/industrial_telemetry_orm.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

# 2. Establish the Async Engine (The bridge to the database)
DATABASE_URL = f"sqlite+aiosqlite:///{DB_PATH}"
engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True prints the raw SQL it generates

# 3. Create the Session Factory
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)

# 4. The Declarative Base Class (All tables inherit from this)
class Base(DeclarativeBase):
    pass


# 5. Define the Table as a Python Class
class SensorLog(Base):
    __tablename__ = "sensor_logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    machine_id = Column(String, nullable=False)
    temperature = Column(Float, nullable=False)
    anomaly_flag = Column(Boolean, default=False)
    # Use timezone-aware UTC times for production-grade logging
    logged_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))


# 6. Initialization Script
async def init_orm_db():
    print("=== INITIALIZING ORM DATABASE ===")
    # Create all tables defined by classes that inherit from Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # Insert a record using the Object-Oriented approach
    async with AsyncSessionLocal() as session:
        new_log = SensorLog(
            machine_id="BOSCH_ASSEMBLY_ARM_02",
            temperature=45.2,
            anomaly_flag=False,
        )
        session.add(new_log)
        await session.commit()
        # Because expire_on_commit=False, attributes remain available after commit
        print(f"Record successfully mapped and saved! ID assigned: {new_log.id}")


if __name__ == "__main__":
    asyncio.run(init_orm_db())
