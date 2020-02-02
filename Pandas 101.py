# -*- coding: utf-8 -*-
#Creating Dataframes
'''
import pandas as pd
data = [['A',10],['B',12],['C',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df
'''
#Creating Dataframes with datatype
'''
import pandas as pd
data = [['A',10],['B',12],['C',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
print df
'''
#Indexed Dataframes
'''
import pandas as pd
data = {'Name':['A', 'B', 'C', 'D'],'Age':[10,12,13,15]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
'''

#DATAFRAMES AND NAN(Not A Number)
'''
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'c'])
print df1
print df2
'''
#COLUMN ADDITION,Deletion
'''
import pandas as pd
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([10, 20, 30], index=['a', 'b', 'c'])}
df = pd.DataFrame(d)
df['three']=pd.Series([100,200,300],index=['a','b','c'])
df['four']=df['one']+ df['two']+df['three']
print df
#del df['four']
#print df
'''
#Appending ROWS and Deleting it
'''
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
print df
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])
df = df.append(df2)
print df

# Drop rows with label 0
#df = df.drop(0)
#print df
'''
