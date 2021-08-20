mycursor = mydb.cursor()


class insertIntoDB(tableName, rowName[])
    sql = "INSERT INTO " tableName "(" rowName[] ") VALUES (%s)"
    val = ("John", "Highway 21")
    mycursor.execute(sql, val)
    mydb.commit()

print(mycursor.rowcount, "record inserted.")
