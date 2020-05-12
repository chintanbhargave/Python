import psycopg2


def create():
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres543' host='localhost' port='5432' ")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()


def insert(it,qty,pr):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres543' host='localhost' port='5432' ")
    cursor = con.cursor()
    cursor.execute("INSERT INTO store VALUES (%s,%s,%s)", (it,qty,pr))
    con.commit()
    con.close()


def get_data():
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres543' host='localhost' port='5432' ")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM store")
    data = cursor.fetchall()
    con.close()
    return data


def delete(it):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres543' host='localhost' port='5432' ")
    cursor = con.cursor()
    cursor.execute("DELETE FROM store WHERE item=%s",(it,))
    con.commit()
    con.close()

def update(qty,pr,it):
    con = psycopg2.connect("dbname='database1' user='postgres' password='postgres543' host='localhost' port='5432' ")
    cursor = con.cursor()
    cursor.execute("UPDATE store SET quantity=%s, price=%s where item=%s", (qty,pr,it))
    con.commit()
    con.close()

print(get_data())