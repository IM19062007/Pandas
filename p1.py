import pandas as pd
import numpy as np
import os
df=pd.read_csv("Tips.csv",index_col=0)
df1=df.copy(deep=True)#Independent 
df2=df.copy(deep=False)#Dependent

print(df.iat[99,1],type(df.iat[99,1]))
print('*'*100)
print(df)
print('*'*100)
print('Size',df.size)
print('Shape',df.shape)
print('No. of dimension',df.ndim)
n=int(input('Enter the number of rows\n'))
print('First',n,'rows\n',df.head(n))
print('Last',n,'rows\n',df.tail(n))
print('*'*100)
print('Columns',df.columns)
print('Rows',df.index)
print('*'*100)
print(df.info())
m=pd.DataFrame(df.describe())
print(m)
r1=m.index
c1=m.columns
print('*'*100)
print('Rows',r1)
print('Columns',c1)
print('*'*100)

c2=int(input('Columns(0-2): '))
r2=int(input('Rows(0-7): '))
l=[]
for c in range(0,3):
    l.append((m.iat[2,c])**2)
print(l)


print(m)
print('Variance',l[0],l[1],l[2])







