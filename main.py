from operations import (add_student,
                        view_all_students,
                        search_students,
                        delete_student,
                        update_student,
                        show_statistics)
from file_handler import load_student

def show_menu():
    print("\n" + "-"*40)
    print(" Student Management System💻")
    print("-"*40)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

def main():

    print("\n Welcome to Student Management System")

    students = load_student()

    print(f"📂 Loaded {len(students)} student(s) from storage.")

    is_running = True
    while is_running:
        try:

            show_menu()

            choice = int(input("Enter Your Choice(1-7):"))

            if choice == 1:
                add_student(students)
            elif choice == 2:
                view_all_students(students)
            elif choice == 3:
                search_students(students)
            elif choice == 4:
                update_student(students)
            elif choice == 5:
                delete_student(students)
            elif choice == 6:
                show_statistics(students)
            elif choice == 7:
                print("Thank you for using this program")
                is_running = False
            else:
                print("Invalid Choice, please enter valid choice !!!")

        except ValueError:
            print("Input must be integer(1-7) !!!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()