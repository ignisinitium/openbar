import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="tearsfor_openBar",
  password="yourpassword"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)