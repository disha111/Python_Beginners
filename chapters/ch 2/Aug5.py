import sqlite3
from db import Employee

conn = sqlite3.connect("employee.db")
print("DB is Created...")
conn.execute(''' create table if not exists emp(
    fname text,
    lname text,
    pay integer
    )
    ''')
print("Table is Created...")
############## INSERT #########################
#conn.execute("insert into emp values('{}','{}','{}')".format('Disha','Vaghela',50000))
#print("Record is added...")
#conn.execute("insert into emp values (?,?,?)",('Disha','Vaghela',10000))

#conn.execute("insert into emp values (:fname,:lname,:pay)",{'fname':'RKU','lname':'SOE','pay':465789})
pay = 10000
lname = 'Vaghela'
############# UPDATE #############
#conn.execute("update emp set pay = ? where lname = ?",(pay,lname))

#################### DELETE ###############
fname = 'RKU'
#conn.execute("delete from emp where fname = :fname ",{'fname':fname})

c = conn.execute("select * from emp")
print(c.fetchall())
conn.commit()
conn.close()