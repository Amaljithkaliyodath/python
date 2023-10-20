student={}
regno=100
studentli=[]
teacher={}
teacherlist=[]
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
              for i in studentli:
                     for j,k in i.items():

                        print(j,';',k)
    if choice==3:
         teachername=input('enter teacher name')
         teacher['teachername']=teachername
         teachdepartment=input('enter teaching department')
         teacher['teacherdepartment']=teachdepartment
         teacherlist.append(teacher.copy())
    elif choice==4:    
                  for i in teacherlist:
                       for j,k in i.items():
                           print(j,';',k)
            
    elif choice==5:  
        stdname=input('enter student name')           
        student['stdname']=stdname
    elif choice==6:
   
           exit()