import random as r
import csv
import os

print("------Student Record Management System------")
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
    print("Menu:")
    print("╔══════════════════════════════════════════════╗")
    print("║ [1] Add Student Details                      ║")
    print("║ [2] Delete Student Details                   ║")
    print("║ [3] Modify Student Details                   ║")
    print("║ [4] Search Student Details                   ║")
    print("║ [5] Sort Student Records                     ║")
    print("║ [6] View all Records                         ║")
    print("║ [7] Save Changes                             ║")
    print("║ [8] Revert Changes                           ║")
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
    print(
        f"Student: {name}, has been added to the records, with admission no:{add_num}\n"
    )


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
            print(student, "\n")
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


def sortStudent(record):
    l = sorted(record.items())
    record.clear()
    record.update(dict(l))
    print("Student Record has been sorted.")


def showStudent(record):
    max_name_length = max(len(record[i]['Name']) for i in record)
    max_class_length = max(len(record[i]['Class']) for i in record)

    print("Student Records:")

    space = (21 + (max_name_length + 4 if max_name_length > 4 else 8) +
             (max_class_length + 4 if max_class_length > 5 else 9))
    spacen = max_name_length + 4 if max_name_length > 4 else 8
    spacec = max_class_length + 4 if max_class_length > 5 else 9

    print("╒" + "═" * space + "╕")
    print(f"│{'Admission Number':^19}│{'Name':^{spacen}}│{'Class':^{spacec}}│")
    print("╞" + "═" * space + "╡")

    for i in record.keys():
        admission_number = record[i]['Admission Number']
        name = record[i]['Name']
        student_class = record[i]['Class']

        print(
            f"│{admission_number:^19}│{name:^{spacen}}│{student_class:^{spacec}}│"
        )

        if i == list(record.keys())[len(list(record.keys())) - 1]:
            print("╘" + "═" * space + "╛")
        else:
            print("├" + "─" * space + "┤")
    print("\n")


def load_records(file_name="record.txt"):
    record = {}
    try:
        with open(file_name, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    admission_number = int(row["Admission Number"])
                    record[admission_number] = {
                        "Admission Number": admission_number,
                        "Name": row["Name"],
                        "Class": row["Class"]
                    }
                except (ValueError, KeyError) as e:
                    print(f"Error processing row {row}: {e}")
    except FileNotFoundError:
        print(
            f"Error: '{file_name}' file not found. Starting with an empty record."
        )
    except Exception as e:
        print(f"Unexpected error while loading records from {file_name}: {e}")
    return record


def save_records(record, file_name="record.txt"):
    try:
        with open(file_name, "w", newline="") as f:
            fieldnames = ["Admission Number", "Name", "Class"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for student in record.values():
                writer.writerow(student)
    except Exception as e:
        print(f"Error saving records to {file_name}: {e}")


def auto_save(record):
    save_records(record, "record_temp.txt")


def check_unsaved_changes():
    if os.path.exists("record_temp.txt"):
        while True:
            choice = input(
                "Unsaved changes detected. Do you want to restore them? (y/n): "
            ).strip().lower()
            if choice == 'y':
                return load_records("record_temp.txt")
            elif choice == 'n':
                print("Discarding unsaved changes.")
                os.remove("record_temp.txt")
                return load_records("record.txt")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    return load_records("record.txt")


record = check_unsaved_changes()

while True:
    try:
        display_menu()
        choice = input("Enter your choice: ")
        print("-" * 60)
        print("\n")
        if choice == '1':
            addStudent(record)
            auto_save(record)
        elif choice == '2':
            removeStudent(record)
            auto_save(record)
        elif choice == '3':
            modifyStudent(record)
            auto_save(record)
        elif choice == '4':
            searchStudent(record)
        elif choice == '5':
            sortStudent(record)
            auto_save(record)
        elif choice == '6':
            showStudent(record)
        elif choice == '7':
            save_records(record, "record.txt")
            print("Changes have been saved.")
        elif choice == '8':
            record = load_records("record.txt")
            os.remove("record_temp.txt")
            print("Changes have been reverted to the last saved state.")
        elif choice == '0':
            if os.path.exists("record_temp.txt"):
                while True:
                    save_choice = input(
                        "Do you want to save changes before exiting? (y/n): "
                    ).strip().lower()
                    if save_choice == 'y':
                        save_records(record, "record.txt")
                        os.remove("record_temp.txt")
                        print("Changes have been saved. Exiting the program.")
                        break
                    elif save_choice == 'n':
                        print("Exiting without saving changes.")
                        os.remove("record_temp.txt")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            break
        else:
            print("Invalid choice. Please try again.\n\n")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 60)
