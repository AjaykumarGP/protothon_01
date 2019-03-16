import math

while(1):
    i=input("Enter the numeber series in comma seperated values")
    ser=i.split(",")
    ser2=[]
    n=len(ser)
    for i in ser:
        i=float(i)
        ser2.append(i)
    s=0
    print(ser2)
    for i in ser2:
        s=s+i**2
    mean=s/n
    
    
    sqt=math.sqrt(mean)
    print("RMS value of the given number series is",sqt)