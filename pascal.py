x=input("Enter the height of the pascal triangle")
x=int(x)
l=[1]
for i in range(x):
    print(l)
    newli=[]
    newli.append(l[0])
    for j in range(len(l)-1):
        newli.append(l[j]+l[j+1])
    newli.append(l[-1])
    l=newli
    