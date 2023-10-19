bank={}
account_no=1234565
balance=0
new=[]
acc=[]
while True:
    print('''
          1.create acc
          2.view acc
          3.add balance
          4.withdraw balance
          5.exit''')
    choice=int(input('enter your choice'))
    if choice==1:
        name=input('enter your name')
        bank['name']=name
        age=int(input('enter your age'))
        bank['age']=age
        contact_no=int(input('enter your contact number'))
        bank['contact_no']=contact_no
        bank['account_no']=account_no
        account_no=account_no+1
        bank['balance']=balance
        new.append(bank.copy())
    elif choice==2:
        for i in new:
         print('-'*20)
         for j,k in i.items():
              print(j,';',k)
              for i in range(1):
                   print('-'*20)
    elif choice==3:
        account_no=int(input('enter your account_no'))
        amount=int(input('enter your amount'))
      
        for i in new:
            acc.append(i["account_no"])

        if account_no in acc:
                for i in new:
                     
                  if i['account_no']==account_no:
                    i['balance']+=amount
                  else:
                    print('acc not found')
    elif choice==4:
         account_no=int(input('enter your account_no'))
         amount=int(input('enter your amount'))

         for i in new:
              acc.append(i["account_no"])
    
         if account_no in acc:
                for i in new:   
                  if i['account_no']==account_no:
                    if i['balance']>=amount:
                     i['balance']-=amount
                    else:
                         print('money not found')
         else:
               print('acc not found')


    elif choice==5:
   
             exit()


             


