def display_menu():
    print("\nMenu:")
    print("1. Add a Student")
    print("2. Delete a Student")
    print("3. Modify a Student Details")
    print("4. Search a Student")
    print("5. Sort the Students")
    print("6. Display the Records")
    print("0. Exit")


def addStudent(lst):
    name = input("Enter the name of contact: ")
    num = int(input("Enter the number of contact: "))
    lst.append([name, num])
    print(f"Student {name} has been added to the directory.")


def removeStudent(lst):
    element = input("Enter the element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"{element} has been deleted from the list.")
    else:
        print(f"{element} is not in the list.")


def searchStudent(lst):
    element = input("Enter the element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"{element} has been deleted from the list.")
    else:
        print(f"{element} is not in the list.")


def modifyStudent(lst):
    position = int(
        input(
            "Enter the position of the element to modify (starting from 0): "))
    if 0 <= position < len(lst):
        new_element = input("Enter the new element: ")
        lst[position] = new_element
        print(
            f"Element at position {position} has been modified to {new_element}."
        )
    else:
        print(
            f"Invalid position. Please enter a position between 0 and {len(lst)-1}."
        )


def sortStudent(lst):
    lst.sort()
    print("The list has been sorted.")


def showStudent(lst):
    print("The current list is:")
    for i, element in enumerate(lst):
        print(f"{i}: {element}")


lst = []
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        addStudent(lst)
    elif choice == '2':
        removeStudent(lst)
    elif choice == '3':
        modifyStudent(lst)
    elif choice == '4':
        searchStudent(lst)
    elif choice == '5':
        sortStudent(lst)
    elif choice == '6':
        showStudent(lst)
    elif choice == '0':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
