a=[1,2,3,]
b=[]
target=2
if target in a:
    for i in range(0,len(a)):
        if a[i]==target:
            b.append(i)
    else:
            print("[-1,-1]")