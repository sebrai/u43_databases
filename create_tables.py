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
    database = 'musikk'
)
mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE artists (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL)')
mycursor.execute('CREATE TABLE albums (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, artist_id INT NOT NULL, FOREIGN KEY (artist_id) REFERENCES artists(id))')
mycursor.execute('CREATE TABLE songs (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50) NOT NULL, genre VARCHAR(50),length_min INT NOT NULL, artist_id INT NOT NULL, album_id INT NOT NULL, FOREIGN KEY (artist_id) REFERENCES artists(id), FOREIGN KEY (album_id) REFERENCES albums(id))')
for info in mycursor:
    print(info)