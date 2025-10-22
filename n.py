import mysql.connector

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
mycursor.execute('USE musikk')
mycursor.execute('DROP TABLE albums')

for info in mycursor:
    print(info)