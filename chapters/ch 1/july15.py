############################ PUBLIC PRIVATE AND PROTECTED EXAMPLE ############################################
class student:
    _name = None
    _roll = None
    __college = None
    myvar = "RKU1"
    def __init__(self,name,roll,college):
        self._name = name
        self._roll = roll
        self.__college = college
        
    @classmethod
    def change_myvar(cls):
        cls.myvar = "RK University"
        print(cls.myvar)
    def _displayroll(self):
        print("roll : ",self._roll)
    def __privatefun(self):
        print("college : ",self.__college)
    def accessprivatefun(self):
        self.__privatefun()
class CEIT(student):
    def __init__(self,name,roll,college):
        student.__init__(self,name,roll,college)
    def display(self):
        """self._name = "Disha"#variable of the CEIT class
        self._roll = "19SOECE13021"#variable of the CEIT class
        self.__college = "RK"#variable of the CEIT class"""
        print(self._name,"\n",self._roll)
        #print(self.__college) variable of the CEIT class
        self._displayroll()
        #self.__privatefun() Private method of parent class
        self.accessprivatefun()
obj = CEIT('test','12','RKU')
obj.display()
s1 = student("name",123,"RKU")
student.change_myvar()

# 1. Normal method or instant method
# 2. class Method
# is used for changing the state of class->class variables
# 3. static method
# independent method -> 
