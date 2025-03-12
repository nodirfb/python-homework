# 4. Display the Name and Age of everyone in the table classified as Bajoran.
import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

cursor.execute("""
select name, age from roster
where species = 'Bajoran'
""")

print(cursor.fetchall())