# a=int(input('enter a limit'))
# sum=0
# for i in range(a):
#  b=int(input('enter a element'))
#  sum+=b
 


#  count the no of duplicate elements  in list 
# a=[1,1,1,3,3,2,4,5,6,7,4,4]
# c=0
# for i in set(a):
#  b=a.count(i)
#  if b>1:
#     print(i,b,*a)



a="abababababab"
c=0
for i in a:
  if i=='a':
    c=c+1
    if i=='b':
      c=c-1
    elif c==0:
      print('balanced')
    else:
      print("not balanced")




 