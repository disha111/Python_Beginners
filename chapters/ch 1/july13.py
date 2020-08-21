####################MULTIPLE INHERITANCE ###################
class father:
    father_name = None
    def __init__(self):
        print("Class father Constructor")
    def fathername(self):
        print("Father Name ",self.father_name)
class mother:
    mother_name = None
    def __init__(self):
        print("Class mother Constructor")
    def mothername(self):
        print("Father Name ",self.mother_name)
class son(father,mother):
    son_name = None
    def __init__(self):
        print("Class son Constructor")
    def sonname(self):
        print("Father Name ",self.son_name)
    def display(self):
        self.mother_name = "ABC"
        self.father_name = "PQR"
        print("Father Name : ",self.father_name," and Mother Name : ",self.mother_name)
"""a = son()
a.display()
a.fathername()
a.mothername()"""

############################ MultiLevel #################################
class grandfather:
    g_father = None
    def grandfathername(self):
        print("Father Name ",self.g_father)
class father(grandfather):
    father = None
    def fathername(self):
        print("Father Name ",self.father)
class son(father):
    son = None
    def sonname(self):
        print("Father Name ",self.son)
    def display(self):
        self.g_father = "ABC"
        self.father = "XYZ"
        self.son = "PQR"
        print("GrandFather Name is :",self.g_father," \n Father Name is : ",self.father,"\n Son Name is : ",self.son)
sun = son()
#sun.display()
############################### Access Specifier ################################### PUBLIC PRIVATE PROTECTED

class g_father:
    __gfather_name = None
    def __gfather(self):
        print(self.__gfather_name)
class father(g_father):
    father_name = None
    def father(self):
        print(self.father_name)
class son(father):
    def display(self):
        self.father_name = "ABC"
        self.__gfather_name = "PQRS"
        print("Father Name is : ",self.father_name,"GraandFather Name is : ",self.__gfather_name)
obj = son()
obj.display()
#obj.gfather()
    