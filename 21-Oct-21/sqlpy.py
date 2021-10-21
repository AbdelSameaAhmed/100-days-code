import sqlite3

db = sqlite3.connect('dbtest1.db')

# db.execute("CREATE TABLE if not exists users (id INTEGER NOT NULL PRIMARY KEY,name TEXT NOT NULL,age INTEGER NOT NULL,salary real DEFAULT 500)")
cur = db.cursor()
cur.execute("INSERT INTO users (id, name,age, salary) VALUES(12, 'asa', 33, 500)")
db.commit()