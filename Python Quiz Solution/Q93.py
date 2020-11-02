from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
slices = [59219,55466,47544,36443,35917]
lables = ['JavaScript','HTML/CSS','SQL','Python','Java']
explode=[0,0,0,0.1,0]
plt.pie(slices,labels=lables,explode=explode,wedgeprops={'edgecolor':'black'})
plt.title('My pie chart')
plt.show()