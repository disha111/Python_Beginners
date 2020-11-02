import sqlite3
conn = sqlite2.connect("emp.db")
data = conn.execute("select * from emp")
print("data")