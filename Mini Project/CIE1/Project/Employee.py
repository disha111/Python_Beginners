#1
from validation import Validation
from PermanentEmployee import Per_Emp
from connect import myconnect
class Employee:
      _empname=""
      _emptype=""
      _empemail=""
      _empsalary=""
      def __init__(self):
            self._empname = input("enter name: ")
            self._empemail=input("enter email: ")
            e = Validation()
            if(e.validateemail(self._empemail) == False):
                  exit(0)
            self._empmob=input("enter mobile no: ")
            if(e.validatemobile(self._empmob) == False):
                  exit(0)
            self._emptype = input("enter type: ")
            self._empexp = int(input("enter experience: "))
            self._empsalary = self.getsalary()
            
      def getsalary(self):
            if self._emptype=="P" or self._emptype=="p":
                  Opemp = Per_Emp()
                  return Opemp.calculatesalary(self._empexp)
            else:
                  print("Invalid Employee. Please enter only 'p' or 'P'")
      #3
      @staticmethod
      def addnote():
            note = input("Enter Your Notes Here \n")
            fopen = open("notes.txt","a")
            fopen.write("\n")
            fopen.write(note)
            fopen.close()
print("1. Add Emp")
print("2. Display Emp")
print("3. Add Notes")
choice = int(input("Enter your Choice:"))
if choice == 1:
      c = Employee()
      obj = myconnect()
      obj.savetodb(c._empname,c._empemail,c._empmob,c._emptype,c._empexp,c._empsalary)
elif choice==2:
      obj = myconnect()
      obj.display()
elif choice==3:
      Employee.addnote()
else:
      print("invalid choice")