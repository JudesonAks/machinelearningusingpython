# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:15:44 2020

@author: admin1
"""
#Reading Excelvalues
'''
df = pd.read_csv('a.csv')
print df
df['D']= df['A']+ df['B']+df['C']
print df
df.to_csv('b.csv')
'''
#Numpy rounding
'''
import numpy as np 
a = np.array([1.0343,5.635, .0723, 0.567, 25.532]) 

#print np.around(a) 
print np.around(a, decimals = 1) 
print np.around(a, decimals = 2) 
'''
#TRIGNOMETRIC
'''
import numpy as np 
a = np.array([15,30,45,60,90]) 
print 'Array containing sine values:' 
sin = np.sin(a*np.pi/180) 
print sin 
print '\n'  
print 'Compute sine inverse of angles. Returned values are in radians.' 
inv = np.arcsin(sin) 
print inv 
print '\n'  
print 'Check result by converting to degrees:' 
print np.degrees(inv)  
b = np.array([0.25, 1.33, 1, 12, 100])   
print 'After applying reciprocal function:' 
print np.reciprocal(b) 
c = np.array([10,100,1000]) 
print 'Applying power function:' 
print np.power(c,2)
'''
#Exponential
#numpy.real() − returns the real part of the complex data type argument.
#numpy.imag() − returns the imaginary part of the complex data type argument.
#numpy.conj() − returns the complex conjugate, which is obtained by changing the sign of the imaginary part.
'''
a = np.array([-5.6j, 0.2j, 11. , 1+1j]) 
print 'Our array is:' 
print a 
print '\n'  

print 'Applying real() function:' 
print np.real(a) 
print '\n'  

print 'Applying imag() function:' 
print np.imag(a) 
print '\n'  

print 'Applying conj() function:' 
print np.conj(a) 
print '\n'  
'''
#NUMPY RANGING
'''
import numpy as np
a=np.arange(2,12)
print (a)
#a1=np.arange(2,12,3)
#print (a1)
#b=np.random.rand(5)
#print (b)
#c=np.random.randint(5,100,5)
#print (c)
'''