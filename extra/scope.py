#global variable
a = 10 
b = 9
c = 11
print("Global Variables A =",a,", B =",b,", C =",c)
print("ID of var B :",id(b))
def something():
    global a
    a = 15 
    b = 5 #local variable
    globals()['c'] = 16 #changing the global value.
    x = globals()['b']
    print("\nLocal Variables A =",a,", B =",b,", C =",c,", X =",x)
    print("Inside func the ID of var B :",id(x))
    print('In func from global to local var A changed :',a)
    print('In func local var B :',b)
    print('In func local var (X) accessing global var B :',x)
    
something()
print('Outside the func global var (A) remains Changed :',a)
print('Outside the func after changing global var C :',c)