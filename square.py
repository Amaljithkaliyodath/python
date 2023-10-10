n=int(input("enter a number"))
while (n%2==0):
    n /=2
    if n==1:
        print('true')
    else:
        print('false')