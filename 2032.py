n1=[1,2,3]
n2=[4,3,3,2]
n3=[5,3]
n=[]
for i in n1:
    for j in n2:
        if i==j:
            n.append(i)
            
        elif j==i:
            n.append(j)
            for k in n3:
                if i==k or j==k:
                    n.append(k)
                    b=set(n)
                    c=list(b)
                    print(c)