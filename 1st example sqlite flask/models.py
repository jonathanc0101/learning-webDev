#database commmunication file between app.py and database.db

from os import path
import sqlite3

ROOT = path.dirname(path.relpath(__file__))

def createPost(name, content):
    con = getConnection()
    cur = con.cursor()
    cur.execute("insert into posts (name,content) values(?,?)", (name, content))
    con.commit()
    con.close()

def getPosts():
    con = getConnection()
    cur = con.cursor()
    cur.execute("select * from posts")
    
    ##closing the connection??
    # con.close()

    posts = cur.fetchall()
    return posts
    
def getConnection() -> str:
    return sqlite3.connect(path.join(ROOT, "database.db"))