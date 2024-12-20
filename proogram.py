import random as r

banner = """
 █████╗  ██████╗ █████╗ ██████╗ ██╗ ██████╗ ███╗   ██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔═══██╗████╗  ██║
███████║██║     ███████║██║  ██║██║██║   ██║██╔██╗ ██║
██╔══██║██║     ██╔══██║██║  ██║██║██║   ██║██║╚██╗██║
██║  ██║╚██████╗██║  ██║██████╔╝██║╚██████╔╝██║ ╚████║
╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═════╝ ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
"""
print(banner)
print("╔══════════════════════════════════════════════╗")
print("║            Welcome to Acadion ERP            ║")
print("╚══════════════════════════════════════════════╝")


def display_menu():
    print("╔══════════════════════════════════════════════╗")
    print("║ [1] Add a Student                            ║")
    print("║ [2] Delete a Student                         ║")
    print("║ [3] Modify a Student Details                 ║")
    print("║ [4] Search a Student                         ║")
    print("║ [5] Sort the Students                        ║")
    print("║ [6] Display the Records                      ║")
    print("║ [0] Exit                                     ║")
    print("╚══════════════════════════════════════════════╝")


def addmission_num():
    return r.randint(100000, 999999)


def addStudent(record):
    print("Add records of student")
    name = input("Enter name : ")
    std = input("Enter class : ")
    add_num = addmission_num()
    record[add_num] = {
        "Addmission Number": add_num,
        "Name": name,
        "Class": std
    }
    print(f"Student {name} has been added to the records.\n")


def removeStudent(record):
    element = input("Enter the name of student to delete: ")
    for i in list(record.keys()):   
        if element in record[i]["Name"]:
            del record[i]
            print(f"{element} has been deleted from the list.")
            break
        else:
            print(f"{element} is not in the list.")


def searchStudent(record):
    element = input("Enter the name of student to search: ")
    for i in list(record.keys()):
        if element in record[i]["Name"]:
            print(record[i])


def modifyStudent(record):
    position = int(
        input(
            "Enter the position of the element to modify (starting from 0): "))
    if 0 <= position < len(record):
        new_element = input("Enter the new element: ")
        record[position] = new_element
        print(
            f"Element at position {position} has been modified to {new_element}."
        )
    else:
        print(
            f"Invalid position. Please enter a position between 0 and {len(record)-1}."
        )


def sortStudent():
    global record
    l = list(record.keys())
    l.sort()
    record = {i: record[i] for i in l}
    print("The list has been sorted.")


def showStudent(record):
    print("Student Records:")
    print("╔══════════════════════════════════════════════╗")
    print("║ Addmission Number ||     Name     ||  Class  ║")
    print("╚══════════════════════════════════════════════╝")
    for i in record.keys():
        print(f"║ {record[i]['Addmission Number']}{(17 - len(str(record[i]['Addmission Number']))) *' '} || {record[i]['Name']}{(13 - len(record[i]['Name'])) *' '}|| {record[i]['Class']}{(8- len(record[i]['Class'])) *' '}║")
        print("╚══════════════════════════════════════════════╝")


record = dict()
while True:
    display_menu()
    choice = input("Enter your choice: ")
    print("\n")
    if choice == '1':
        addStudent(record)
    elif choice == '2':
        removeStudent(record)
    elif choice == '3':
        modifyStudent(record)
    elif choice == '4':
        searchStudent(record)
    elif choice == '5':
        sortStudent()
    elif choice == '6':
        showStudent(record)
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
