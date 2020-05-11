import sqlite3


def create():
    con = sqlite3.connect("mylite.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(it,qty,pr):
    con = sqlite3.connect("mylite.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO store VALUES (?,?,?)", (it,qty,pr))
    con.commit()
    con.close()


def get_data():
    con = sqlite3.connect("mylite.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM store")
    data = cursor.fetchall()
    con.close()
    return data


def delete(it):
    con = sqlite3.connect("mylite.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM store WHERE item=?",(it,))
    con.commit()
    con.close()

def update(qty,pr,it):
    con = sqlite3.connect("mylite.db")
    cursor = con.cursor()
    cursor.execute("UPDATE store SET quantity=?, price=? where item=?", (qty,pr,it))
    con.commit()
    con.close()


print(get_data())