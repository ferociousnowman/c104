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

data=Counter(newdata)
modedataforrange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height, occurrence in data.items():
    if 50<float(height)<60:
        modedataforrange['50-60'] += occurrence
    elif 60<float(height)<70:
        modedataforrange['60-70'] += occurrence
    elif 70<float(height)<80:
        modedataforrange['70-80'] += occurrence

moderange,modeoccurrence=0,0
for range,occurrence in modedataforrange.items():
    if occurrence>modeoccurrence:
        moderange,modeoccurrence=[int(range.split("-")[0]),int(range.split("-")[1])],occurrence
mode=float((moderange[0]+moderange[1])/2)
print(mode)