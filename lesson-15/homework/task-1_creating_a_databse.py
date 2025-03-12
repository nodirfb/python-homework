# 1. Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

cursor.execute("""
create table roster(
    name text,
    species text,
    age integer
    )
""")
conn.commit()
conn.close()

