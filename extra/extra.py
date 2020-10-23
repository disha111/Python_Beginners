from matplotlib import pyplot as pt

langs = ['c','c++','python','php','android']
stud =[20,30,80,70,60]
# pt.pie(stud,labels=langs,autopct="%1.2f%%",startangle=90,explode=(0,0,0.1,0,0.1),colors=['r','g','m','b','g'])    
pt.pie(stud,labels=langs,autopct="%1.2f%%",startangle=-45,colors=['r','g','m','b','g'])
pt.savefig('piechart.png')
pt.show()

# girls = [10,20,5,8,4]
# boy = [5,9,3,46,45]
# range = [10,20,30,40,50]
# pt.scatter(range,girls,color='r',marker='*')
# pt.scatter(range,boy,color='b',marker='.')
# pt.show()


# langs = ['c','c++','python','php','android']
# stud =[10,20,80,70,60]

# pt.bar(langs,stud,color=['r','g','b','c','k'],width=0.5)
# pt.yticks([0,10,20,30,40,50,60,70,80,90,100])
# pt.show()