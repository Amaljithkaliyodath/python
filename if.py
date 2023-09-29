# a=int(input('enter your age'))
# if a<=18:
#    print(a,"your are minor")
# elif a<=65:
#    print(a,"your adult")
# else:
#    print('you are a senior citizen')



# a=int(input('enter a number'))
# b=int(input('enter a number'))
# if a>b:
#     print(a,' is largest')
# elif b>a:
#     print(b,' is largest')
# else:
#     print("both are equal")






# a=int(input('enter a number'))
# b=int(input('enter a number'))
# if  a%2:
#     print(a,'is even')
# else:
#     print( a,'is odd')
#     if b%2:
#         print(b,'is even')
#     else:
#      print( b,'is odd')



# a=input('enter a letter')
# str=['a','e','i','o','u']
# if a in str:
#     print(a,' is vowel')
# else:
#     print('a is consonant')


# a=int(input('enter your grade'))
# if a>=90:
#     print(a,"A")
# elif a>=80:
#      print(a,"B")
# elif a>=70:
#       print(a,"C")
# elif a>=60:
#       print(a,"D")
# elif a<=59: 
#      print(a,"F")


# a=int(input('enter'))
# b=int(input('enter'))
# if a,'+','/','*',



# a=int(input('enter your age'))

# if a<=2:
#    print(a,"your are infant")
# elif a<=12:
#     print(a,"your child")
# elif a<=19:
#     print(a,"your teenager")
# elif a<=64:
#     print(a,"your adult")
# elif a>=65:
#     print(a,"your senior")


  

# a=int(input('enter a number'))
# b=int(input('enter a number'))
# c=int(input('enter a number'))
# if a>b and a>c:
#     print('a is larger')
# elif b>a and b>c:
#     print('b is larger')
# elif c>a and c>b:
#     print('c is larger')
# else:
#     print('both are equal')




# a=int(input('enter a number'))
# if a==1:
#     print('sunday')
# elif a==2:
#     print('monday')
# elif a==3:
#     print('tuesday')    
# elif a==4:
#     print('wednesday')
# elif a==5:
#     print('thursday')   
# elif a==6:
#     print('friday')
# elif a==7:
#     print('saturday')




# w=int(input('enter weigth'))
# h=int(input('enter a heigth'))
# b=w/h
# if b<=18.5:
#     print('underweigth')
# elif b<=24.9:
#     print('normal weigth')
# elif b<=29.9:
#     print('overwweigth')
# else:
#     print('obesity')


# a=str((input('enter color')))
# b='red'
# c='green'
# d='yellow'
# if a in c:
#     print('go')
# elif a in b:
#     print('stop') 
# elif a in d:
#   print('proceed with caution')


# a=int(input('enter a time '))
# if a>=5 and a<=11:
#     print('good morning')
# elif a>=12 and a<=16:
#     print('good afternoon')
# elif a>=17 and a<=20:
#     print('good evening')
# elif a>=21 and a<=24:
#     print('good night')
# elif a<=4:
#     print('good night')

a=str(input('enter a character'))
print(a.isdigit())
print(a.isalpha())
print(a.isalnum())
if (a.upper()):
  print(a,'is uppercase')
elif (a.lower()):
  print(a,'is lowercase')
  





# num1=int(input('enter frist number'))
# num2=int(input('enter second number'))
# op=input('enter any operator')
# if op=='+':
#     a=num1+num2
#     print(a)
# elif op=='-':
#     b=num1-num2
#     print (b)
# elif op=='*':
#     c=num1*num2
#     print(c)
# elif op=='/':
#     d=num1/num2
#     print(d)





    
# a=int(input('enter purchase amount'))
# if a>=100:
#     discount=(10/100)*a
#     print(discount)
#     print('amount=',a-discount)
# elif a>=50:
#     discount=(5/100)*a
#     print(discount)
#     print('amount=',a-discount)
# else:
#     print(a)

# a=77
# b=int(input('enter a number '))
# if a<b:
#     print('too high')
# elif a>b:
#     print('too low')
# elif a==b:
#     print('correct')





# a=int(input('enter a year'))
# if a in range(0,3000,4):
#     print('leap year')
# else:
#     print('not a leap year')


# temp=float(input('enter temp'))
# unit=str(input('enter unit(f or c)'))
# if unit=='f':
#     f=(temp*1.8)+32
#     print("f temp ",f)
# elif unit=='c':
#     f=(temp-32)/1.8
#     print("c temp ",f)