import mysql.connector

cnx = mysql.connector.connect(user='tearsfor_openBar', password='574?OB!MYSQL$Pa55', host='127.0.0.1', database='tearsfor_openBar')
cnx.close()

from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'tearsfor_openBar'

TABLES = {}
TABLES['users'] = (
    "CREATE TABLE `users` ("
    "  `user_no` int(11) NOT NULL AUTO_INCREMENT,"
    "  `birth_date` date NOT NULL,"
    "  `first_name` varchar(14) NOT NULL,"
    "  `last_name` varchar(16) NOT NULL,"
    "  `gender` enum('M','F') NOT NULL,"
      "  PRIMARY KEY (`user_no`)"
    ") ENGINE=InnoDB")

query = ("SELECT first_name, last_name, FROM users "
         "WHERE birth_date BETWEEN %s AND %s")

birth_start = datetime.date(1999, 1, 1)
birth_end = datetime.date(1999, 12, 31)

cursor.execute(query, (birth_start, birth_end))

for (first_name, last_name, birth_date) in cursor:
  print("{}, {} was born on {:%d %b %Y}".format(
    last_name, first_name, birth_date))

cursor.close()
cnx.close()