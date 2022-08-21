#!/usr/bin/python


#pip install mysqlclient

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","mysqladmin", "candystore")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM candystore.employees;"

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()

# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()


#INSERT a Record in mysql:

# Open database connection
db = MySQLdb.connect("localhost","root","mysqladmin", "candystore")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = '''INSERT INTO `candystore`.`employees`
(`employee_id`,
`first_name`,
`last_name`,
`hire_date`,
`position`,
`hourly_wage`)
VALUES
(10,
'Sumit',
'Kumar',
'2022-08-20',
'Data Architect',
40);
'''

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()
# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()


#Update a Record in mysql:

# Open database connection
db = MySQLdb.connect("localhost","root","mysqladmin", "candystore")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = '''UPDATE `candystore`.`employees`
SET
`hourly_wage` = 45
WHERE `employee_id` = 6;'''

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()
# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()

#Delete a Record in mysql:

# Open database connection
db = MySQLdb.connect("localhost","root","mysqladmin", "candystore")

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = '''DELETE FROM `candystore`.`employees`
WHERE employee_id >8;'''

# execute SQL query using execute() method.
cursor.execute(sql)

db.commit()
# get the record count updated
print(cursor.rowcount, " record(s) affected")

# disconnect from server
db.close()