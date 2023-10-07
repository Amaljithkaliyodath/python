
a=[2,3,4,1,5]
tar=6
b=[]
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==tar:
            b.append(i)
            b.append(j)
            print(b)