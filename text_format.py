while(1):
    a=input("Enter any sentence\t")
    
    print("Upper case is", a.upper())
    print("Lower case is",a.lower())
    print("Title case is",a.title())
    a=a.split(".")
    ful=""
    for i in range(len(a)):
        ful+=a[i].replace(a[i][0],a[i][0].upper())
        if(i+1<len(a)):
            ful+="."

        
    print("start case",ful)

        
    