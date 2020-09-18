import sqlite3
import re
class Conn:
    def __init__(self):
        self.con = sqlite3.connect("Employee.db")
        self.con.execute(''' create table if not exists employee(
            name text,
            email text,
            m_no text,
            type text,
            salary integer,
            exp integer
            )
            ''')
        self.con.commit()
        self.con.close()
        
    def insert(self,e):
        pattern = re.compile(r"[.\w-]+@[\w.-]+[.\w.-]")
        if(pattern.search(e.email)):
            self.con = sqlite3.connect("Employee.db")
            self.con.execute("insert into employee values (?,?,?,?,?,?)",(e.name,e.email,e.m_no,e.type,e.salary,e.exp))
            self.con.commit()
            self.con.close()
        else:
            print("Enter Valid Email")

    def display(self,id):
        self.con = sqlite3.connect("Employee.db")
        self.c = self.con.execute("select * from employee")
        result = self.c.fetchall()
        print("Name is ",result[id-1][0])
        print("Email is ",result[id-1][1])
        print("Mobile No is ",result[id-1][2])
        print("Job Type is ",result[id-1][3])
        print("Salary is ",result[id-1][4])
        print("Experience is ",result[id-1][4])
        self.con.commit()
        self.con.close()
