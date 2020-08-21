import sqlite3
conn = sqlite3.connect("emp.db")

print("database Created...")

conn.execute(''' create table if not exists emp (
        id integer primary key,
        name text)
''')
print("Table Created...")
conn.commit()
conn.close()