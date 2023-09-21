# find the longest word form a string
a=str(input('enter a word'))
a=a.split(' ')
b=[]
for i in a:
    b.append(len(i))
    print(a[b.index (max(b))])
    


