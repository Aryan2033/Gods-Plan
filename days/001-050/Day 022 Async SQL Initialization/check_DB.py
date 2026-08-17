import sqlite3

conn = sqlite3.connect('factory.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Machines")
rows = cursor.fetchall()
#what is fetchall()? #The fetchall() method is used to retrieve all the rows returned by a SELECT query. It returns a list of tuples, where each tuple represents a row of data from the database. Each element in the tuple corresponds to a column in the result set. If there are no rows returned by the query, fetchall() will return an empty list.

for row in rows:
    print(row)  

#(1, 'CNC 101', 'Berlin')