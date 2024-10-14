import sqlite3

# ## connect to sqlite
connection=sqlite3.connect("student.db")

# ##create a cursor object to insert record,create,table,retrieve

cursor=connection.cursor()

##create the table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A',90)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'B',85)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Sudhanshu', 'Devops', 'C',76)''') 
cursor.execute('''INSERT INTO STUDENT VALUES ('Vikash', 'Data Science', 'C',83)''') 


#Display data inserted
print("Data Inserted in the table:")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

connection.commit()

connection.close()