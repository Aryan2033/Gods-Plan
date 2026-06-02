import sqlite3

conn = sqlite3.connect('factory.db')

cursor = conn.cursor() 
#what is cursor()? #The cursor() method is used to create a cursor object, which allows you to execute SQL commands and queries on the database. It acts as an interface between the Python code and the database, enabling you to interact with the database and retrieve or manipulate data.

cursor.execute(""" CREATE TABLE Machines (
               machine_id INTEGER PRIMARY KEY,
               machine_name TEXT,
               location TEXT)
               """)


cursor.execute("""
               INSERT INTO Machines (machine_name, location) 
               VALUES (?,?)""", ("CNC 101", "Berlin"))

conn.commit() #what is commit()? #The commit() method is used to save the changes made to the database. When you execute SQL commands that modify the database (such as INSERT, UPDATE, DELETE), those changes are not immediately saved to the database file. Instead, they are stored in a temporary area called a transaction. The commit() method is called to finalize the transaction and permanently save the changes to the database. If you do not call commit(), the changes will not be saved and will be lost when the connection is closed.