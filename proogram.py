import random as r


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


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
    print(color.BOLD + " " + color.UNDERLINE + "Menu:" + color.END)
    print("╔══════════════════════════════════════════════╗")
    print("║ [1] Add a Student                            ║")
    print("║ [2] Delete a Student                         ║")
    print("║ [3] Modify a Student Details                 ║")
    print("║ [4] Search a Student                         ║")
    print("║ [5] Sort the Students                        ║")
    print("║ [6] Display the Records                      ║")
    print("║ [0] Exit                                     ║")
    print("╚══════════════════════════════════════════════╝")


def generateAdmission_num():
    return r.randint(100000, 999999)


def addStudent(record):
    print("Add records of student")
    name = input("Enter name : ")
    std = input("Enter class : ")
    add_num = generateAdmission_num()
    record[add_num] = {"Admission Number": add_num, "Name": name, "Class": std}
    print(f"Student {name} has been added to the records.\n")


def removeStudent(record):
    element = input("Enter the name of student to delete: ")
    for admission_number, student in record.items():
        if element.lower() == student["Name"].lower():
            del record[admission_number]
            print(f"{element} has been deleted from the list.\n")
            break
    else:
        print(f"{element} is not in the list.\n")


def searchStudent(record):
    element = input("Enter the name of student to search: ")
    for admission_number, student in record.items():
        if element.lower() == student["Name"].lower():
            print(student)
            break
    else:
        print("Student not found\n")


def modifyStudent(record):
    element = input("Enter the name of student to modify: ")
    for admission_number, student in record.items():
        if element.lower() == student["Name"].lower():
            name = input("Enter new name : ")
            std = input("Enter new class : ")
            student["Name"] = name
            student["Class"] = std
            print("The Record has been modified.\n")
            break
    else:
        print("Student not found\n")


def sortStudent():
    global record
    l = list(record.keys())
    l.sort()
    record = {i: record[i] for i in l}
    print("Student Record has been sorted.")


def showStudent(record):
    max_name_length = max(len(record[i]['Name']) for i in record)
    max_class_length = max(len(record[i]['Class']) for i in record)

    print("Student Records:")

    print("╒" + "═" *
          (19 + 2 + (max_name_length + 4 if max_name_length > 4 else 8) +
           (max_class_length + 4 if max_class_length > 5 else 9)) + "╕")
    print(
        f"│{'Admission Number':^19}│{'Name':^{max_name_length + 4 if max_name_length > 4 else 8}}│{'Class':^{max_class_length + 4 if max_class_length > 5 else 9}}│"
    )
    print("╞" + "═" *
          (19 + 2 + (max_name_length + 4 if max_name_length > 4 else 8) +
           (max_class_length + 4 if max_class_length > 5 else 9)) + "╡")

    for i in record.keys():
        admission_number = record[i]['Admission Number']
        name = record[i]['Name']
        student_class = record[i]['Class']

        print(
            f"│{admission_number:^19}│{name:^{max_name_length + 4 if max_name_length > 4 else 8}}│{student_class:^{max_class_length + 4 if max_class_length > 5 else 9}}│"
        )

        if i == list(record.keys())[len(list(record.keys())) - 1]:
            print("╘" + "═" *
                  (19 + 2 +
                   (max_name_length + 4 if max_name_length > 4 else 8) +
                   (max_class_length + 4 if max_class_length > 5 else 9)) +
                  "╛")
        else:
            print("├" + "─" *
                  (19 + 2 +
                   (max_name_length + 4 if max_name_length > 4 else 8) +
                   (max_class_length + 4 if max_class_length > 5 else 9)) +
                  "┤")
    print("\n\n")


record = dict()
record = {
    125478: {
        "Admission Number": 125478,
        "Name": "Ashish",
        "Class": "8"
    },
    458753: {
        "Admission Number": 458753,
        "Name": "Krishna Singh",
        "Class": "2"
    },
    852456: {
        "Admission Number": 852456,
        "Name": "Preeti",
        "Class": "5"
    },
    625479: {
        "Admission Number": 625479,
        "Name": "Aadhya",
        "Class": "10"
    }
}
while True:
    display_menu()
    choice = input("Enter your choice: ")
    print("-" * 60)
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
        print("Invalid choice. Please try again.\n\n")
