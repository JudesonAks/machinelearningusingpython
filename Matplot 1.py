# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:09:20 2020

@author: admin1
"""
#Plotting
'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4,5,6])
#plt.plot([1,2,3,4,5,6], color='red')
#plt.plot([1,2,3,4,5,6], ":")
#plt.plot([1,2,3,4,5,6], "o")
plt.ylabel('numbers')
plt.show()
'''
#Bargraph
'''
from matplotlib import pyplot as plt 
x = [5,8,10] 
y = [12,16,6]  

x2 = [6,9,11] 
y2 = [6,15,7] 
plt.bar(x, y, color='red',align = 'center') 
plt.bar(x2, y2, color = 'g', align = 'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis') 
plt.xlabel('X axis')  
plt.show()
'''
#Subplot
'''
values = [1, 10, 100]
names = ['group_a', 'group_b', 'group_c']
plt.subplot(1,3,1)
plt.bar(names, values)
plt.subplot(1,3,2)
plt.scatter(names, values)
plt.subplot(1,3,3)
plt.plot(names, values)
plt.show()
'''