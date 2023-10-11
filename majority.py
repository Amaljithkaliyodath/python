a=[1,2,2,3,3,3,3]
b=len(a)
for i in range(b):
    if a.count(i)>b/2:
     print('majority is',i)