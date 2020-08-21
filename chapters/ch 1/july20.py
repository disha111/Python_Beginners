############################### CLASS METHOD OR STATIC METHOD ##########################################
class student:

    college = "RKU"

    def __init__(self,m1,m2,m3):
        self.m1 =m1
        self.m2 = m2
        self.m3 = m3
    def avarage(self):
        return(self.m1+self.m2+self.m3)/3
    @classmethod
    def college_name(cls,name):
        cls.college=name
        return(cls.college)
    @staticmethod
    def info():
        print("This is a Static mehtod of student class...!!")

s1 = student(66,55,99)
s2 = student(56,89,45)
print(s1.avarage())
print(s2.avarage())
print(student.college_name("RK University"))  
print(s1.college_name("RK")) 
print(s2.college_name("University"))  
print(student.college_name("RK University"))
student.info()


#Polymorphysm --> ability to take more then one from 
#overloading  --> methods same name but parameter different
#overriding  -->same but implementation / functionality different.
#overriding  --> python dose not support method overloading

class parent:
    def __init__(self):
        print("this is a parent class")
    def display(self):
        print("Display method of parent class")
    def sum(self,a,b):
        return a+b
    #def sum(self,a=none,b=none,c=none):
     #   return a+b+c
class child(parent):
    def __init__(self):
        print("this is a child method")
    def display(self):
        super().display()
        print("Display method of  child class")
    

p = parent()
c = child()
p.display()
print(p.sum(5,6))
c.display()
