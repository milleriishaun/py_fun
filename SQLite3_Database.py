
'''
# This is how you create a table in SQLite3


import sqlite3
import sys


def printDB():

    try:
        result = theCursor.execute("SELECT ID, FName, LName, Age, "\
            "Address, Salary, HireDate FROM Employees")

        for row in result:
            print("ID: ", row[0])
            print("FName: ", row[1])
            print("LName: ", row[2])
            print("Age: ", row[3])
            print("Address: ", row[4])
            print("Salary: ", row[5])
            print("HireDate: ", row[6])
    
    except sqlite3.OperationalError:
        print("The Table Doesn't Exist")

    except:
        print("Couldn't Retieve Data from Database")

    

db_conn = sqlite3.connect('text.db')
print("Database Created")

# traverse the records of the results

# organize data into table and put in the data types
# issue a a query... RFI
# cursor will traverse through all the information that is returned
theCursor = db_conn.cursor()

# this deletes the table if it was already made
db_conn.execute("DROP TABLE IF EXISTS Employees")
db_conn.commit()

# Wanted to use a try loop because it might error
try:
    # executes a SQL command
    # SQL specific commands are in uppercase
    # inside Employees Table, it will have a unique ID as an integer
    # and it will be marked as a Primary Key(this unique key differntiates each
    # row of data) because we need unique things inside of here.
    # Also want a number to increment, autoincrement. We'll say that the
    # value cannot be Null. The ID has to be unique and cannot have no value/null.
    # 5 datatypes: NULL, INTEGER, TEXT, REAL, BLOB(binary data)
    db_conn.execute("CREATE TABLE Employees(ID INTEGER PRIMARY KEY "\
    "AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, LName TEXT NOT NULL, "\
    "Age INTEGER NOT NULL, Address TEXT, Salary REAL, HireDate TEXT);")

    # commit has the things executed
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table Couldn't Be Created")

print("Table Created")

# This hows how to insert data into the table
# Cursor can be used to execute these commands too, but using SQL commands
# works as well
# This inserts an employee in the database
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, "\
    "Salary, HireDate) VALUES ('Shaun', 'Miller', 77, '123 Main St.', "\
    "100000000, date('now'))")
db_conn.execute("INSERT INTO Employees (FName, LName, Age, Address, "\
    "Salary, HireDate) VALUES ('Kyson', 'Nguyen', 99, '123 Main St.', "\
    "100000000, date('now'))")
db_conn.commit()




# Print all the stuff we have stored in the database
printDB()

# Now we want to update things in the database
try:
    # check if unique
    # The SET Address is the thing that is actually updated
    db_conn.execute("UPDATE Employees SET Address = '222 Main St.' WHERE ID=1")
    db_conn.commit()
    print("Table UPDATED")

except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")

printDB()
'''



'''
try:
    db_conn.execute("DELETE FROM Employees WHERE ID=1")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")

printDB()

# as if we did not delete the name
db_conn.rollback()
'''




'''
# You can add new Columns
# for employees, we can put an image in...
# image with a default value of null
try:
    db_conn.execute("ALTER TABLE Employees ADD COLUMN 'Image'"\
        " BLOB DEFAULT NULL")
    db_conn.commit()

except sqlite3.OperationalError:
    print("Table Couldn't Be Updated")

# We can also retrieve our Database Table names
# And to do that we have to use the Table, and run execute
theCursor.execute("PRAGMA TABLE_INFO(Employees)")

# now we can fetch all, which returns all the data that we need
# Using a list comprehension for this is like the right thing because
# there is a lot of information and we want it come out as a list.
rowNames = [nameTuple[1] for nameTuple in theCursor.fetchall()]

print(rowNames)

# Sometimes useful to get all the rows
# Get the total number of rows
theCursor.execute("SELECT COUNT(*) FROM Employees")
# theCursor.fetchall gives back a list of lists
numOfRows = theCursor.fetchall()
print("Total Rows: ", numOfRows[0][0])

# Get the SQLite version number.
# Get one result with fetchone()
theCursor.execute("SELECT SQLITE_VERSION()")
print("SQLite Version: ", theCursor.fetchone())

# You can get DictionaryCursor to get data from a dictionary
with db_conn:
    db_conn.row_factory = sqlite3.Row
    # Call the cursor again
    theCursor = db_conn.cursor()
    # Select everything from Table
    theCursor.execute("SELECT * FROM Employees")
    # Call for a new cursor
    rows = theCursor.fetchall()

    # Cycle through the results and print it out
    for row in rows:
        print("{} {}".format(row["FName"], row["LName"]))

# How to write files to a file... in case need to dump database info to a file
with open('dump.sql', 'w') as f:
    # line is a string
    for line in db_conn.iterdump():
        f.write("%s\n" % line)

printDB()



# Always want to close the DB after usage.
db_conn.close()
print("Database Closed")
'''




# real tutorials on SQLite3(from 2013)
# embedded relational database
# database is part of the code, not outside resource
# runs on any machine w/any software... good for Android Apps
# complicated queries might make it fail, but there are a lot of extensions
# they can be used in any language

import sqlite3
import sys

