import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tearsfor_openBar",
  password="4S}b]L6B-~b(",
  database="tearsfor_openBar"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, firstName VARCHAR(255),lastName VARCHAR(255), streetAddress VARCHAR(255), state VARCHAR(255), $

mycursor.execute("SHOW TABLES")
  for x in mycursor:
  print(x)


