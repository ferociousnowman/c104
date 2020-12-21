import pandas as pd
import csv 
from collections import Counter 
with open ('height-weight.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    nnumber=filedata[i][1]
    newdata.append(nnumber)
n=len(newdata)
newdata.sort()
if n%2==0:
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]
    print(n)
print('median:'+str(median))
