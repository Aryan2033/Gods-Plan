from sqlalchemy import (
    create_engine, 
    Column, 
    Integer,
    String
        )

from sqlalchemy.orm import (
    declarative_base,
    sessionmaker
)

#declarative base is a factory function that constructs a base class for declarative class definitions
# sessionmaker is a factory for creating new Session objects, which are used to interact with the database

Base = declarative_base()

class Machine(Base):
    __tablename__ = 'engines'

    engine_id = Column(Integer, primary_key=True)
    engine_name = Column(String)
    location = Column(String)

system = create_engine('sqlite:///factory2.db')
Base.metadata.create_all(system)


Session = sessionmaker(bind=system)
# in short sessionmaker is a factory for creating new Session objects, which are used to interact with the database.  
session = Session() 

new_engine = Machine(engine_name='CNC 101', location='Berlin')
session.add(new_engine)
session.commit() 

# We use SQLAlchemy because it gives you a cleaner, safer, and more scalable way to work with databases in Python.

# In practice, it helps with:

# Avoiding raw SQL for every operation
# Preventing SQL injection with parameter handling
# Switching between databases more easily, like SQLite, PostgreSQL, or MySQL
# Managing connections, sessions, and transactions properly
# Working with tables as Python objects instead of only SQL strings
# Writing complex queries while still keeping the code organized




engines = session.query(Machine).all()


for engine in engines:
    print(engine.engine_id, engine.engine_name, engine.location)
#1 CNC 101 Berlin