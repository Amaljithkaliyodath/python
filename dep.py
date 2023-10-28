students = []
teachers = []
regno = 100

while True:
    print('''
          1. Student 
          2. Teacher
          3. View Students
          4. View Teachers
          5. Assign Teacher
          6. View Department
          7. Check Fee Balance
          8. Students under Teacher
          9. Exit''')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        student = {}
        student['stdname'] = input('Enter student name: ')
        student['stdage'] = int(input('Enter student age: '))
        student['stddepartment'] = input('Enter student department: ')
        student['regno'] = regno
        student['teachstore'] = None  # Initialize teachstore key for each student
        regno += 1
        students.append(student)

    elif choice == 2:
        teachers.append(input('Enter teacher name: '))

    elif choice == 3:
        print(students)

    elif choice == 4:
        print(teachers)

    elif choice == 5:
        student_name = input('Enter student name: ')
        teacher_name = input('Enter teacher name to assign: ')
        found = False
        for student in students:
            if student['stdname'] == student_name:
                student['teachstore'] = teacher_name
                found = True
                break
        if not found:
            print('Student not found.')

    elif choice == 6:
        department = input('Enter department: ')
        for student in students:
            if student['stddepartment'] == department:
                print('Student Name:', student['stdname'])
                print('Assigned Teacher:', student.get('teachstore', 'Not Assigned'))

    elif choice == 7:
        student_name = input('Enter student name: ')
        found = False
        for student in students:
            if student['stdname'] == student_name:
                amount = int(input('Enter your amount: '))
                depamount = 10000 - amount
                print('Balance amount =', depamount)
                found = True
                break
        if not found:
            print('Student not found.')

    elif choice == 8:
        teacher = input('Enter teacher name: ')
        students_under_teacher = []
        for student in students:
            if student['teachstore'] == teacher:
                students_under_teacher.append(student['stdname'])
        print('Students under', teacher, ':', students_under_teacher)

    elif choice == 9:    
        exit()
