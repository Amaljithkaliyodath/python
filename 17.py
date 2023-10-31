a={
    2:"abc",
    3:"def",
    4:"ghi",
    5:"jkl",
    6:"mno",
    7:"pqrs",
    8:"tuv",
    9:"wxyz"
}
b=int(input("enter a number"))
c=b//10
d=b%10
num=a[c]
num1=a[d]
for i in num:
    for j in num1:
        print(i+j)
