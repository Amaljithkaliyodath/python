a=[1,0,0,12,5]
for i in a:
    if i==0:
     a.remove(i)
     a.append(i)
print(a)