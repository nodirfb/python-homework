# 3. Update the Name of Jadzia Dax to be Ezri Dax
import sqlite3

conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

cursor.execute("""
update roster
set name = 'Ezri Dax'
where name = 'Jadzia Dax'
""")

conn.commit()
conn.close()