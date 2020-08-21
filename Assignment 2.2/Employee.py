from Connection import Conn
class Employee:
    def __init__(self,name=None,email=None,m_no=None,salary=None,type=None,exp=None):
        self.name = input("Enter  Name : ")
        self.email = input("Enter Email : ")
        self.m_no = input("Enter Mobile No : ")
        self.type = input("Enter Job Type : ")
        self.salary = input("Enter Salary : ")
        self.exp = input("Enter Experience : ")
print("1. Add Employee")
print("2. Display Employee")
print("3. Add Notes")
print("4. Exit")
ch = int(input("Enter Your Choice : "))
while(ch!=4):
    if ch == 1:
        e= Employee()
        c = Conn()
        c.insert(e)
    elif ch == 2:
        id = int(input("Enter ID "))
        c = Conn()
        c.display(id)
    else:
        print(1)
    ch = int(input("Enter Your Choice : "))
