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

# qeuries the user of the program
insert_choice= input("what do you want to add: \033[32martist\033[0m , \033[32malbum\033[0m , \033[32msong\033[0m: ")
match insert_choice:
    case "song":
        song_name = input("what is the song called?: ")
        song_artist = input("who made the song?: ")
        song_album = input("whitch album is it in?: ")
        y_n_genre = input("does the song fitt into a genre: (y/n): ")
        t_f_genre = False
        if y_n_genre =="y":
            t_f_genre = True
            song_genre = input("whitch genre does it fit into?: ")
        song_len = int(input("how many seconds does the song last? (awnser with a number, exsample: 1,5 minutes = 90): "))
    case "album":
        alb_name = input("what is the albums name?: ")
        alb_artist = input("who made the song?: ")
    case "artist":
        ar_name = input("what is the artist called?: ")
    case _:
        print(f"\033[31m \"{insert_choice}\" \033[0m is not a valid option")
        sys.exit()

# inserts new info into the db
match insert_choice:
    case "artist":
        sql = "INSERT INTO artists (name) VALUES (%s)"
        mycursor.execute(sql,(ar_name,))
        mycursor.execute("SELECT * FROM artists")
    case "album":
        mycursor.execute("SELECT id FROM artists WHERE name = %s",(alb_artist,))

        result = mycursor.fetchone()

        if result:
            art_id = result[0]
        else:
            print(f"\033[31m \"{alb_artist}\" \033 does not exist in database, reboot program choose \" artist\" and ad in the artist to this database")
            sys.exit()
        sql = "INSERT INTO albums (name,artist_id) VALUES (%s,%s)"
        val = (alb_name,art_id)
        mycursor.execute(sql,val)
        mycursor.execute("SELECT * FROM albums")
    case "song":
        mycursor.execute("SELECT id FROM artists WHERE name = %s",(song_artist,))
        artist_result = mycursor.fetchone()
        if artist_result:
            s_artist_id = artist_result[0]
        else:
            print(f"\033[31m \"{song_artist}\" \033 does not exist in database, reboot program choose \" artist\" and ad in the artist to this database")
            sys.exit()
        mycursor.execute("SELECT id FROM albums WHERE name = %s",(song_album,))
        album_result = mycursor.fetchone()
        if album_result:
            s_album_id = album_result[0]
        else:
            print(f"\033[31m \"{song_album}\" \033 does not exist in database, reboot program choose \" album\" and ad in the album to this database")
            sys.exit()
        if t_f_genre:
            sql = "INSERT INTO songs (name,artist_id,album_id,genre,length_sec) VALUES (%s,%s,%s,%s,%s)"
            val = (song_name,s_artist_id,s_album_id,song_genre,song_len)
            mycursor.execute(sql,val)
        else:
            sql = "INSERT INTO songs (name,artist_id,album_id,length_sec) VALUES (%s,%s,%s,%s)"
            val = (song_name,s_artist_id,s_album_id,song_len)
            mycursor.execute(sql,val)
        mycursor.execute("SELECT * FROM songs")
#print info
for info in mycursor:
    print(info)

#helps make sure that the data is accepted into the database permanently
mycursor.fetchall()
mydb.commit()
