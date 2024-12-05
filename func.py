import random as r

def addmission_num():
    return r.randint(100000,999999)

record = []

def addStudent():
    print("Add records of student")
    name = input("Enter name : ")
    clas = input("Enter class : ")
    add_num = addmission_num()
    record.append(dict(name = name,clas = clas,addmission_number = add_num))

def displayRecord():
    print(record)

def deleteStudent():
    name = input("Enter name of student to be deleted: ")
    for i in record:
        if i[0] == name:            
            record.remove(i)


def menu():
    print (""""
    1.Add a Student
    2.Delete a Student
    3.Display Student Details
    4.Exit/Quit
    5.Change Student Details
    6.Enter marks
    """)
    ans=input("What would you like to do?")
    if ans=="1":
        addStudent()
        print("\nStudent Added") 
    elif ans=="2":
        deleteStudent()
        print("\n Student Deleted") 
    elif ans=="3":
        displayRecord()
        print("\n Student Record Found") 
    elif ans=="4":
        print("\n Goodbye")
        return 0
    elif ans !="":
        print("\n Not Valid Choice Try again")

    return 1

while True:
    a = menu()
    if a == 0:
        break
    
