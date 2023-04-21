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

# Needs Error checkiing to not remake a database
cursor.execute("CREATE DATABASE NiaLab_Tempature")


cursor.execute("USE NiaLab_Tempature")

# Needs error checing to not duplicate table
cursor.execute("CREATE TABLE TEMP1 (Date_current INT, Time_current INT, Tempature INT)")
cursor.execute("CREATE TABLE TEMP2 (Date_current INT, Time_current INT, Tempature INT)")
               
               
# code to insert data into document
sql = "INSERT INTO TEMP1 (Date, Time, Tempature) VALUES (%s, %d, %d)"
val = (10102023, 2148, 74)
cursor.execute(sql, val)
mydb.commit()

print(cursor.rowcount, "record inserted.")
 


