import sqlite3
class myconnect:
      
      def __init__(self):
            #4
            self.conn = sqlite3.connect("emp.db")
            #5      
            self.conn.execute('''create table is not exist emp (
                  ename text,
                  eemail text,
                  emob integer,
                  etype text,
                  eexp integer,
                  esalary integer
            )''')
                  
      def savetodb(self,ename,eemail,emob,etype,eexp,esalary):
            #6

      def display(self):
            #7