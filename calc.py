

while(1):
    in1=float(input("Enter the first operand"))
    in2=float(input("Enter the second operand"))

    print("\n1.Addition")
    print("\n2.Subtraction")
    print("\n3.Multiplication")
    print("\n4.Division")
    
    
    op=input("Enter operation number")
    if (op=="1"):
        
        print(in1+in2)
    elif(op=="2"):
        
        print(in1-in2)
    elif(op=="3"):
        print(in1*in2)
    elif(op=="4"):
        if in2==0:
            print("Denominator should not be zero")
            continue
        else:
            print(in1/in2)
    

