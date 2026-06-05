from sqlalchemy import create_engine, select
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



#insert another sensor log entry
sensor = SensorLog(machine_id=2, temperature=30.0, timestamp="2024-06-01 13:00:00")

with Session(engine) as session:
    session.add(sensor) # this adds the sensor object to the session, which is a temporary storage area for objects that are being added to the database.
    session.commit() # this commits the transaction, which means that the changes made to the database (in this case, adding the sensor object) are saved permanently.


#read data with orm 
logs = session.query(SensorLog).all()


#or with sqlalchmey 2.0


results = session.execute(select(SensorLog))

logs2  = results.scalars().all() 
#what scalars() does is to extract the SensorLog objects from the results of the query, and all() is used to get a list of all the SensorLog objects that were returned by the query.
#without scalars(), the results would be a list of tuples, where each tuple contains a SensorLog object and any other columns that were selected in the query. By using scalars(), we can get a list of just the SensorLog objects, which is often more convenient when we are only interested in the objects themselves.

    