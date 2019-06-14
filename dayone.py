import matplotlib.pyplot as plt
'''x=[1,2,3,4,5]
y=[1,4,9,16,25]
plt.scatter(x,y,s=200)
plt.show()'''
x_values=list(range(1,5001))
y_values=[x**3 for x in x_values]
#plt.scatter(x_values,y_values,s=40,c=(0.5,0.5,0))
plt.scatter(x_values,y_values,s=40,c=y_values,cmap=plt.cm.Reds)
#颜色映射  y的大小来映射  蓝色 红色可以
#plt.axis([0,5500,0,111100000])
plt.savefig('example1.jpg',bbox_inches='tight')
plt.show()
