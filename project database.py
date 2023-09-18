import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE record")

print("record database created successfully!")
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="record"
)

mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE entries (
                   Sno INT,
                   UUID VARCHAR(255),
                   IPaddress FLOAT,
                   Machine VARCHAR(255),
                   Version INT,
                   NodeName VARCHAR(255)
                   )""")

print("entries table created successfully!")
