student={}
teacher={}
regno=1001
studentli=[]
while True:
    print('''
          1.student name
          2.view
          3.teachers
          4.exit''')
    choice=int(input('enter your choice'))
    if choice==1:
        stdname=input('enter student name')
        student['stdname']=stdname
        stdage=int(input('enter student age'))
        student['stdage']=stdage
        student['regno']=regno
        regno=regno+1
        studentli.append(student.copy)
    if choice==2:
          print(studentli)
    if choice==3:
         teachername=input('enter teacher name')
         teacher['teachername']=teachername
        