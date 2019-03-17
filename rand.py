import csv
import os
import random
j=1
for i in range(1,4):
    k=open(f"myfile{i}.csv","x")
    a= [['#', 'NUM1','NUM2','NUM3','NUM4','NUM5']]
    while os.stat(f"myfile{i}.csv").st_size<2048:
a.append([j,random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101),random.randint(1,101)])
    j=j+1
    with open(f"myfile{i}.csv",'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(a)