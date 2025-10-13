import random as r
import csv
import os

print("----------Student Record Management System----------")
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


def generateAdmission_num(record):
    while True:
        num = r.randint(100000, 999999)
        if num not in record:
            return num


def addStudent(record):
    print("Enter details of the Student: ")
    student = {}
    add_num = generateAdmission_num(record)
    student["Admission Number"] = add_num

    student["Name"] = input("→ Name: ").title()
    student["Class"] = input("→ Class: ")
    student["Section"] = input("→ Section: ").upper()
    student["DOB"] = input("→ Date of Birth (DD-MM-YYYY): ")
    student["Gender"] = input("→ Gender (Male/Female): ").title()
    student["Parent Name"] = input("→ Parent Name: ").title()
    student["Address"] = input("→ Address: ").title()

    record[add_num] = student

    print(f"\nStudent: {student['Name']}, has been added to the records, with admission no:{student['Admission Number']}\n")


def removeStudent(record):
    try:
        element = int(input("Enter the Admission Number of Student to Delete: "))
    except ValueError:
        print("Invalid admission number.\n")
        return
    
    if element in record:
        del record[element]
        print(f"{element} has been deleted from the record.\n")
    else:
        print(f"{element} is not in the Records.\n")


def searchStudent(record):
    field = input("Search by (Name/Class/Admission Number): ").title().strip()
    value = input(f"Enter {field}: ").strip()

    results = {
        adm_no: s
        for adm_no, s in record.items()
        if str(s.get(field, "")).lower() == value.lower()
    }

    if results:
        showStudent(results)
    else:
        print("No records found.")


def modifyStudent(record):
    try:
        element = int(input("Enter the Admission Number of Student to Modify: "))
    except ValueError:
        print("Invalid admission number.\n")
        return
    
    student = record.get(element)
    if not student:
        print("Student not found.\n")
        return
    
    print("Leave the field blank to keep existing value.\n")
    for key in ["Name", "Class", "Section", "DOB", "Gender", "Parent Name", "Address"]:
        new_value = input(f"→ {key} ({student[key]}): ").strip()
        if new_value:
            student[key] = new_value.title()

    print("The Record has been modified.\n")


def sortStudent(record):
    if not record:
        print("No records to sort.")
        return
    
    field = input("Enter field to sort by (Admission Number/Name/Class): ").title()

    if field == "Class":
        sorted_records = dict(sorted(record.items(), key=lambda x: (x[1]["Class"], x[1]["Section"])))
    else:
        sorted_records = dict(sorted(record.items(), key=lambda x: x[1].get(field, "")))

    record.clear()
    record.update(sorted_records)
    print(f"Records sorted by {field}.")


def showStudent(record):
    if not record:
        print("No student records to display.\n")
        return

    headers = ["Admission Number", "Name", "Class", "Section", "DOB", "Gender", "Parent Name", "Address"]
    rows = [
        [
            str(student.get('Admission Number', '')),
            student.get('Name', ''),
            student.get('Class', ''),
            student.get('Section', ''),
            student.get('DOB', ''),
            student.get('Gender', ''),
            student.get('Parent Name', ''),
            student.get('Address', '')
        ] for student in record.values()
    ]
    
    col_widths = []
    for i in range(len(headers)):
        max_len = len(headers[i])
        for row in rows:
            max_len = max(max_len, len(str(row[i])))
        col_widths.append(max_len)

    def border(left, fill, sep, right):
        return left + sep.join([fill * (w + 2) for w in col_widths]) + right

    top    = border("╔", "═", "╤", "╗")
    header = "║" + "│".join(f" {headers[i]:^{col_widths[i]}} " for i in range(len(headers))) + "║"
    mid    = border("╠", "═", "╪", "╣")
    bottom = border("╚", "═", "╧", "╝")

    print("\nStudent Records:")
    print(top)
    print(header)
    print(mid)
    for idx, row in enumerate(rows):
        print("║" + "│".join(f" {row[i]:^{col_widths[i]}} " for i in range(len(headers))) + "║")
        print(border("╟", "═", "╪", "╢") if idx < len(rows) - 1 else bottom)
    print()


def load_records(file_name="record.csv"):
    record = {}
    try:
        with open(file_name, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    record[int(row["Admission Number"])] = row
                except (ValueError, KeyError) as e:
                    print(f"Error processing row {row}: {e}")
    except FileNotFoundError:
        print(f"Error: '{file_name}' file not found. Starting with an empty record.")
    except Exception as e:
        print(f"Unexpected error while loading records from {file_name}: {e}")
    return record


def save_records(record, file_name="record.csv"):
    try:
        with open(file_name, "w", newline="") as f:
            fieldnames = ["Admission Number", "Name", "Class", "Section", "DOB", "Gender", "Parent Name", "Address"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for student in record.values():
                writer.writerow(student)
    except Exception as e:
        print(f"Error saving records to {file_name}: {e}")


def auto_save(record):
    save_records(record, "record_temp.csv")


def check_unsaved_changes():
    if os.path.exists("record_temp.csv"):
        while True:
            choice = input("Unsaved changes detected. Do you want to restore them? (y/n): ").strip().lower()
            if choice == 'y':
                return load_records("record_temp.csv")
            elif choice == 'n':
                print("Discarding unsaved changes.")
                os.remove("record_temp.csv")
                return load_records("record.csv")
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    return load_records("record.csv")


record = check_unsaved_changes()

while True:
    try:
        display_menu()
        choice = input("Enter your choice: ").strip()
        print("-" * 60 + "\n")

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
        elif choice == '7':
            save_records(record, "record.csv")
            if os.path.exists("record_temp.csv"):
                os.remove("record_temp.csv")
            print("Changes have been saved.")
        elif choice == '8':
            record = load_records("record.csv")
            if os.path.exists("record_temp.csv"):
                os.remove("record_temp.csv")
            print("Changes have been reverted to the last saved state.")
        elif choice == '0':
            if os.path.exists("record_temp.csv"):
                while True:
                    save_choice = input("Do you want to save changes before exiting? (y/n): ").strip().lower()
                    if save_choice == 'y':
                        save_records(record, "record.csv")
                        os.remove("record_temp.csv")
                        print("Changes have been saved. Exiting the program.")
                        break
                    elif save_choice == 'n':
                        print("Exiting without saving changes.")
                        os.remove("record_temp.csv")
                        break
                    else:
                        print("Invalid input. Please enter 'y' or 'n'.")
            break
        else:
            print("Invalid choice. Please try again.\n\n")

        if choice in ['1','2','3','5']:
            auto_save(record)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    print("-" * 60)
