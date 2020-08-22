import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn = sqlite3.connect("emp.db")
            #5      
            try:
                  self.conn.execute('''create table emp (
                        ename text,
                        eemail text,
                        emob integer,
                        etype char,
                        eexp integer,
                        esalary integer
                  )''')
            except:
                  pass
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6
            self.conn.execute("insert into emp values(?,?,?,?,?,?)",(ename,eemail,emob,etype,eexp,esalary))
            self.conn.commit()

      def display(self):
            self.conn = sqlite3.connect("emp.db")
            id = int(input("Enter id : "))
            record = self.conn.execute("select * from emp")
            result = record.fetchall()
            print("Name is :",result[id-1][0])
            print("Email is :",result[id-1][1])
            print("Mobile Number is :",result[id-1][2])
            print("Job Type is :",result[id-1][3])
            print("Experience is :",result[id-1][4])
            print("Salary is :",result[id-1][5])
            self.conn.commit()
            #7
            # print("Email is :",record.fetchall()[id-1][1])
            # print("Mobile Number is :",record.fetchall()[id-1][2])