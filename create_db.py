import mysql.connector
# create db 
try:
    with open("password.txt","r")  as f:
        password = f.read()
except FileNotFoundError:
    print("password file doesnt exist")

mydb = mysql.connector.connect(
    host = "10.200.14.13",
    port= 3306,
    user = 'extsebrai',
    password = password, 
)
mycursor = mydb.cursor()

#lager database
mycursor.execute('CREATE DATABASE musikk CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci')

#velger at den nye databasen blir brukt
mycursor.execute('USE musikk')


#show created tables
mycursor.execute('SHOW TABLES')
for info in mycursor:
    print(info)