students=[]
def record():
    name=input('Enter Student Name:')
    id=input('Enter Student Id no:')
    age=int(input('Enter student age:'))
    grade=input("Enter grade(A to Z):")
    students.append(name)
    students.append(id)
    students.append(age)
    with open('student_rocord.txt','a') as file:
        file.write(str(students))
        file.write('\n')
def view():
    id_num=int(input('Enter Id no:'))
    with open('student_rocord.txt','r') as file:
        for list in file:
            if list[1]==id_num:
                print(list)
            else:
                print('Student not found')
def menu():
    while True:
        print(
        '\n1.Enter record \n'
        '2.View record\n'
        '3.Exit\n'
        )
        user=int(input('Choose option (1 to 3):'))
        if user==1:
            record()
        elif user==2:
            view()
        elif user==3:
            break
        else:
            print('Enter a valid number')
menu()