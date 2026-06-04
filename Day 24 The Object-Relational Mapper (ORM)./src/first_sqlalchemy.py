from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

class Base(DeclarativeBase):


    pass



engine = create_engine("sqlite:///sensor_logs.db", echo=True) # this creates a connection to a SQLite database called sensor_logs.db. The echo=True argument tells SQLAlchemy to log all the SQL statements that it executes, which can be useful for debugging.

class SensorLog(Base):

    __tablename__ = "sensor_logs"

    id : Mapped[int] = mapped_column(primary_key=True) # what mapped and mapped_column do is to tell SQLAlchemy that this is a column in the database and that it should be mapped to the id attribute of the SensorLog class. The primary_key=True argument tells SQLAlchemy that this column is the primary key of the table.

    machine_id : Mapped[int]  # this is another column in the database that will be mapped to the machine_id attribute of the SensorLog class.

    temperature : Mapped[float]  # this is another column in the database that will be mapped to the temperature attribute of the SensorLog class.
    
    timestamp : Mapped[str]  # this is another column in the database that will be mapped to the timestamp attribute of the SensorLog class.

Base.metadata.create_all(engine)

sensor = SensorLog(machine_id=1, temperature=25.5, timestamp="2024-06-01 12:00:00") # this creates an instance of the SensorLog class with the specified values for machine_id, temperature, and timestamp.

with Session(engine) as session:
    session.add(sensor) # this adds the sensor object to the session, which is a temporary storage area for objects that are being added to the database.
    session.commit() # this commits the transaction, which means that the changes made to the database (in this case, adding the sensor object) are saved permanently.

