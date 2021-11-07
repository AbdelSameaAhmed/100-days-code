# this is sqlite connection code 

import sqlite3
from sqlite3 import connect
conn=sqlite3.connect(r'C:\Users\asahmed\Documents\GitHub\100DaysOfCode\dbtest1.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT exists test_table(id_dep, name_dep, max_salary,min_salary)")








