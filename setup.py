import sqlite3

db = sqlite3.connect("database.db")

cur = db.cursor()

cur.execute("create table roots (root text primary key, definition text, derivation text)")

db.commit()
db.close()