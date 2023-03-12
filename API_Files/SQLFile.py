# Importing module
import mysql.connector
 
# Creating connection object
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "dhED26dL"
)
 
# Printing the connection object
print(mydb)

# Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# cursor.execute("CREATE DATABASE geeks3")

cursor.execute("USE geeks3")
cursor.execute("CREATE TABLE UserInfo (name VARCHAR(255), password VARCHAR(255))")

# code to insert data into document
sql = "INSERT INTO UserInfo (name, password) VALUES (%s, %s)"
val = ("John", "Highway 21")
cursor.execute(sql, val)
mydb.commit()

print(cursor.rowcount, "record inserted.")
 


