import sqlite3
from record import *
from inventory import *

def create_db():
    con=sqlite3.connect(database=r'database.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS inventory(pid text,desc text,ql text,unit text,qp text,loc text,supp text)")
    con.commit()

 



create_db()


















