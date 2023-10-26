student={}
regno=100
studentli=[]
teachlist={}
teachstore=[]
studentstore=[]
while True:
    print('''
          1.student name
          2.viewstudent
          3.teachers
          4.viewteachere
          5.exit''')
    choice=int(input('enter your choice'))
    if choice==1:
        stdname=input('enter student name')
        student['stdname']=stdname
        stdage=int(input('enter student age'))
        student['stdage']=stdage
        stddeppartment=input('enter student department')
        student['stddepartment']=stddeppartment
        student['regno']=regno
        regno=regno+1
        studentli.append(student.copy())
    if choice==2:
             name=input('enter your name')         
             teachlist.append(name)
        
    if choice==3:
        print(studentli)
    if choice==4:    
             print(teachlist)       
    if choice==5: 
             student=input('enter student name') 
             for i in studentli:          
                   studentstore.append(i["name"])
             b=len(teachlist)
             for j in range(b):
                    if student in studentstore:
                         for i in studentli:
                               if i["name"]==student:
                                i["teacher"]=teachlist[j]
                    print(studentli)
    if choice==6:
   
           exit()