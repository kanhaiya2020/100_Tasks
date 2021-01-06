import pymysql
import datetime
# Python 3 code to demonstrate the 
# working of MD5 (string - hexadecimal) 

import hashlib 

# Creation of database

# create table (user) for User in the database (user_db)
create_table_user = "create table user ( \
            Username VARCHAR (100) NOT NULL UNIQUE, \
            Email VARCHAR (100) NOT NULL UNIQUE,  \
            Password VARCHAR (100) NOT NULL , \
            Created_date DATETIME,  \
            Updated_date DATETIME,  \
            PRIMARY KEY ( Username ));" 

mydb = pymysql.connect(
    host = "localhost", # <Your localhost>
    user = "root", # <Your Username>
    passwd = ""  # <Your Password>
    )  # To connect mysql server on localhost

mycursor = mydb.cursor()

# Check database exist or not:
mycursor.execute("SHOW DATABASES")
db_list = list(mycursor.fetchall())
if ('user_db',) not in db_list:
    mycursor.execute("CREATE DATABASE user_db")
    mydb1 = pymysql.connect(
        host = "localhost", 
        user = "root", 
        passwd = "",
        db = "user_db"  # <Your Database Name>
        )
    mycursor1 = mydb1.cursor()
    mycursor1.execute("SHOW TABLES")
    table_list = list(mycursor1.fetchall())
    if ('user',) not in table_list:
        mycursor1.execute(create_table_user)
        print('table is created')
    else:
        print('table is already exist')
    mydb1.close()
else:
    mydb1 = pymysql.connect(
        host = "localhost", 
        user = "root", 
        passwd = "",
        db = "user_db"  # <Your Database Name>
        )
    mycursor1 = mydb1.cursor()
    mycursor1.execute("SHOW TABLES")
    table_list = list(mycursor1.fetchall())
    if ('user',) not in table_list:
        mycursor1.execute(create_table_user)
        print('table is created')
    else:
        print('table is already exist')
    mydb1.close()

mydb.close()
    

# insert the data into table of database, creation and updation of database 

username = input("Enter the username")
password = input("Enter the password")
mail_id = input("Enter the mail")

# For date:
current_datetime = datetime.datetime.now()
Created_date = str(current_datetime)
Updated_date = str(current_datetime)


# For encrypt the Password using md5 alogorithem:

# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(password.encode()) 
encrypted_passwd = result.hexdigest()
print(encrypted_passwd)

per_opr = pymysql.connect(
        host = "localhost", 
        user = "root", 
        passwd = "",
        db = "user_db"  # <Your Database Name>
        )

per_opr_mycursor = per_opr.cursor()

query_for_insert_data = "INSERT INTO user (Username, Email, Password, Created_date, Updated_date) VALUES (%s, %s, %s, %s, %s)"
per_opr_mycursor.execute(query_for_insert_data, (username, mail_id, encrypted_passwd, Created_date, Updated_date))
per_opr.commit()
per_opr.close()
print("data is inserted successfully")

