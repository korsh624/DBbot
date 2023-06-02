import sqlite3
def create_table():
   conn = sqlite3.connect('test.db')
   cur = conn.cursor()
   cur.execute("""CREATE TABLE IF NOT EXISTS users(
               userid INT PRIMARY KEY,
               username TEXT);
               """)
   conn.commit()
   cur.close()
   conn.close()

def add_user():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    userid=int(input('введите id '))
    username=input('Введите имя пользователя ')
    data=(userid, username)
    cur.execute("""INSERT INTO users(userid, username) VALUES (?,?)""", data)
    conn.commit()
    conn.close()

def get_user():
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    id=int(input('Введите id '))
    user = cur.execute(f"""SELECT * FROM users WHERE userid = {id}""").fetchone()
    print(user)

create_table()
add_user()
get_user()