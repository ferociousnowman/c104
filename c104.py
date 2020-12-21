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
    newdata.append(float(nnumber))

n=len(newdata)
total=0
for x in newdata:
    total+=x
mean=total/n
print("mean:"+str(mean))