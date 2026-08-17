from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select

engine = create_async_engine("sqlite+aiosqlite:///sensor_logs.db", echo = True) # this creates a connection to a SQLite database called sensor_logs.db using the aiosqlite driver, which allows for asynchronous database operations. The echo=True argument tells SQLAlchemy to log all the SQL statements that it executes, which can be useful for debugging.

class Base(DeclarativeBase):
    pass

async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all) # this creates the tables in the database based on the metadata defined in the Base class and its subclasses. The run_sync method is used to run the create_all method synchronously, which is necessary because create_all is not an asynchronous method.


SessionLocal = async_sessionmaker(
    bind=engine, # this binds the sessionmaker to the engine, which means that any sessions created by this sessionmaker will use the connection provided by the engine to interact with the database.
    expire_on_commit=False,# this tells SQLAlchemy not to expire the objects in the session after a commit, which means that they will still be available for use after the commit is complete. This can be useful in some cases where you want to continue working with the objects after they have been committed to the database.
    class_=AsyncSession # this tells SQLAlchemy to use the AsyncSession class for the sessions created by this sessionmaker, which allows for asynchronous database operations.
)


class SensorLog(Base):
    __tablename__ = "sensor_logs"

    id : Mapped[int] = mapped_column(primary_key=True),
    machine_id : Mapped[int],
    temperature : Mapped[float],


async with SessionLocal() as session:

        sensor = SensorLog(machine_id=1, temperature=25.5)

        session.add(sensor) 

        await session.commit() 

result = await session.execute(select(SensorLog))
logs = result.scalars().all()