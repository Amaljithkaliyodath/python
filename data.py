student={}
regno=100
studentli=[]
teachlist=[]
teachstore=[]
studentstore=[]
while True:
    print('''
          1.student 
          2.teachers
          3.viewstudent
          4.viewteachere
          5.asign
          6.viewdepartment
          7.exit''')
    choice=int(input('enter your choice'))
    if choice==1:
        name=input('enter student name')
        student['stdname']=name
        age=int(input('enter student age'))
        student['stdage']=age
        stddeppartment=input('enter student department')
        student['stddepartment']=stddeppartment
        student['regno']=regno
        regno=regno+1
        studentli.append(student.copy())
    if choice==2:
             name=input('enter teacher name')         
             teachlist.append(name)
        
    if choice==3:
        print(studentli)
    if choice==4:    
             print(teachlist)       
    if choice==5: 
             student=input('enter student name') 
             for i in studentli:          
                   studentstore.append(i['name'])
             b=len(teachlist)
             for j in range(b):
                    if student in studentstore:
                         for i in studentli:
                               if i['name']==student:
                                i['teachstore']=teachlist[j]
                    # print(studentli)
             for i in studentli:
              print('-'*20)
              for j,k in i.items():
                  print(j,';',k)              
              print('-'*20)
    if choice==6:
           student=input('enter department')
           for i in studentli:
                  studentstore.append(i['stddepartment'])


           if student in studentstore:
              for i in studentli: 

                   if i['stddepartment']==student:
                        for n in teachlist:

                               i['teachstore']=teachlist[0]     
                   else:
                               i['teachstore']=teachlist[1]
           for i in studentli:
             print('-'*20)
             for j,k in i.items():
               print(j,';',k)              
             print('-'*20)  

    if choice==7:
           exit()
