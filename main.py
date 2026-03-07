from pandas import read_pickle


def show_menu():
    print("\n" + "-"*40)
    print("Welcome to Student Management System💻")
    print("-"*40)
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Statistics")
    print("7. Exit")

def main():
    is_running = True
    while is_running:
        try:
            show_menu()

            choice = int(input("Enter Your Choice(1-7):"))

            if choice == 1:
                pass
            elif choice == 2:
                pass
            elif choice == 3:
                pass
            elif choice == 4:
                pass
            elif choice == 5:
                pass
            elif choice == 6:
                pass
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