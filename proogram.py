import random as r

a = """
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░      ░░░░      ░░░░      ░░░       ░░░        ░░░      ░░░   ░░░  ░
▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒  ▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒▒  ▒▒▒▒  ▒▒    ▒▒  ▒
▓  ▓▓▓▓  ▓▓  ▓▓▓▓▓▓▓▓  ▓▓▓▓  ▓▓  ▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓▓  ▓▓▓▓  ▓▓  ▓  ▓  ▓
█        ██  ████  ██        ██  ████  █████  █████  ████  ██  ██    █
█  ████  ███      ███  ████  ██       ███        ███      ███  ███   █
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
"""
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
    '''print("--Welcome to Acadion--")
    print("\nMenu:")
    print("1. Add a Student")
    print("2. Delete a Student")
    print("3. Modify a Student Details")
    print("4. Search a Student")
    print("5. Sort the Students")
    print("6. Display the Records")
    print("0. Exit")'''


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
    element = input("Enter the element to delete: ")
    if element in record:
        record.remove(element)
        print(f"{element} has been deleted from the list.")
    else:
        print(f"{element} is not in the list.")


def searchStudent(record):
    element = input("Enter the element to delete: ")
    if element in record:
        record.remove(element)
        print(f"{element} has been deleted from the list.")
    else:
        print(f"{element} is not in the list.")


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


def sortStudent(record):
    record.sort()
    print("The list has been sorted.")


def showStudent(record):
    print("Student Records:")
    for i in record.keys():
        print("╔══════════════════════════════════════════════╗")
        print("║ Addmission Number ||   Name   ||    Class    ║")
        print("╚══════════════════════════════════════════════╝")
        for key in record:
            print(
                f"║ {record[key]['Addmission Number']}{(17 - len(record[key]['Addmission Number'])) *' '}|| {record[key]['Name']}{(17 - len(record[key]['Name'])) *' '}"
            )
            print(f"║ {record[key]['Name']}")
            print(f"║ {record[key]['Class']}")
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
        sortStudent(record)
    elif choice == '6':
        showStudent(record)
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
