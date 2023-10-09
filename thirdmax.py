a=[1,2]
if len(a)>2:
    b=max(a)
    a.remove(b)
    c=max(a)
    a.remove(a)
    print(max(a))
else:
    print(max(a))