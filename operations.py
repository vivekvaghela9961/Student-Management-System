import json

from student import Student
from file_handler import get_next_id, save_student


def add_student(students):
    print("\n ADD NEW STUDENT")
    print("-"*40)

    while True:
        name = input("Enter student name: ").strip()
        if name:
            break
        else:
            print("Name cannot be empty, please try again.")

    while True:
        try:
            age = int(input("Enter student age: ").strip())
            if 5 <= age <= 100:
                break
            else:
                print("⚠️ Age must be between 5 and 100, please try again.")
        except ValueError:
            print("⚠️ Age must be between 5 and 100")

    grade = input("Enter student grade(eg. A, B, 85%): ").strip().upper()

    subjects_input = input("Enter subjects (comma separated, eg. Maths,Science): ").strip()

    subjects = [subject for subject in subjects_input.split(",") if len(subjects_input)>0]
    if not subjects:
        subjects = ["Not Assigned"]

    new_id = get_next_id(students)

    # now Creating the Student object
    new_student = Student(new_id, name, age, grade, subjects)

    students.append(new_student)

    save_student(students)

    print(f"\n✅ Student '{name}' added with ID: {new_id}")



def view_all_students(students):

    print("\n📋 ALL STUDENTS RECORDS")
    print("-"*40)

    if not students:
        print("❌ No Student found !, Add some first.")
    for student in students:
        student.display()

def search_students(students):

    print("\n🔎 SEARCH STUDENTS")
    print("-"*40)
    print("1. Search by ID")
    print("2.Search by Name")

    choice = input("Enter choice: ").strip()

    results = []
    if choice == "1":
        try:
            student_id = int(input("Enter student ID: "))
            results = [student for student in students if student.student_id == student_id]

        except ValueError:
            print("⚠️  ID must be a number.")
            return

    elif choice == "2":
        try:
            student_name = input("Enter student name: ").strip().lower()
            results = [student for student in students if student_name in student.name.lower().strip()]

        except Exception as e:
            print(e)
            return

    else:
        print("⚠️ Invalid Choice.")

    if results:
        print(f"\n✅ Found {len(results)} student(s):")
        for student in results:
            student.display()

    else:
        print("❌ No student found with that search.")

def delete_student(students):

    print("\n🚮 DELETE STUDENT")
    print("-"*40)

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("⚠️  ID must be a number.")
        return

    else:
        student = None

        for s in students:
            if s.student_id == student_id:
                student = s
                break

        if not student:
            print(f"❌ No student found with ID: {student_id}")
            return

        confirm = input(f"Are you sure you want to delete {student.name}? (y/n) ").strip().lower()

        if confirm == "y":
            students.remove(student)
            save_student(students)
            print(f"✅ Student '{student.name}' deleted.")

        elif confirm == "n":
            print("Delete cancelled.")
            return
        else:
            print("⚠️ Invalid choice.")






def update_student():
    pass

def show_statistics():
    pass