# 2.  Populate your new table with the following values:

# | Name            | Species      | Age |
# |-----------------|--------------|-----|
# | Benjamin Sisko  | Human        |  40 |
# | Jadzia Dax      | Trill        | 300 |
# | Kira Nerys      | Bajoran      |  29 |
import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()


data = [
    ('Benjamin Sisko','Human',40),
    ('Jadzia Dax','Trill',300),
    ('Kira Nerys','Bajoran',29)
]
cursor.executemany('insert into roster values(?,?,?)',data)

conn.commit()
conn.close()