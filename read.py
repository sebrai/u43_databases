import mysql.connector
import sys
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
    database = 'musikk'
)
mycursor = mydb.cursor()
# ^base info required for connection^

# the main code
read_choice= input("withc database should i show?: \033[32martists\033[0m , \033[32malbums\033[0m , \033[32msongs\033[0m: ")
if read_choice in ["artists","albums","songs"]:
    mycursor.execute(f"SELECT * FROM {read_choice}")
else:
    print(f"\033[31m \"{read_choice}\" \033[0m is not a valid option")
    sys.exit()
#print info
for info in mycursor:
    print(info)