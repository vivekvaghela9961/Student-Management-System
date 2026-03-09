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

    subjects = [subject.strip().lower() for subject in subjects_input.split(",") if len(subjects_input)>0]
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


def update_student(students):
    print("\n🔃 UPDATE STUDENT")
    print("-"*40)

    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("ID must be a number.")
        return

    student = None
    for s in students:
        if s.student_id == student_id:
            student = s
            break
    if not student:
        print(f"❌ No student found with ID {student_id}.")
        return

    print("\nCurrent Details:")
    student.display()

    print("\nWhat do you want to update?")
    print("1. Update Name")
    print("2. Update Age")
    print("3. Update Grade")
    print("4. Update Subjects")
    print("5. Cancel Update")

    choice = input("Enter choice: ").strip()
    if choice == "1":
        new_name = input("Enter new student name: ").strip()
        student.name = new_name

    elif choice == "2":
        try:
            new_age = int(input("Enter new student age: ").strip())
            if 5 <= new_age <= 100:
                student.age = new_age
            else:
                print("⚠️ Invalid Age.")
                return
        except ValueError:
            print("Age must be a number.")
            return

    elif choice == "3":
        new_grade = input("Enter new student grade(eg. A, B, 85%): ").strip().upper()
        student.grade = new_grade

    elif choice == "4":
        subjects_input = input("Enter new subjects (Comma Separated): ").strip()
        student.subjects = [subject.strip().lower() for subject in subjects_input.split(",") if len(subjects_input) > 0]

    elif choice == "5":
        print("❌ Update Cancelled.")
        return
    else:
        print("⚠️ Invalid choice.")
        return

    save_student(students)
    print("✅ Student updated Successfully.")



def show_statistics(students):
    print("\n📶 SHOW STATISTICS")
    print("-"*40)

    if not students:
        print("⚠️ No student to analyze.")
        return

    print(f"Total Students: {len(students)}")

    all_subjects = []

    for student in students:
        for subject in student.subjects:
            all_subjects.append(subject)

    unique_subjects = set(all_subjects)
    print(f"Unique Subjects: {len(unique_subjects)}")
    print(f"All Subjects: {', '.join(unique_subjects)}")

    popular_subjects = max(all_subjects, key=all_subjects.count )
    print(f"Most popular Subjects: {popular_subjects}")
    print("-"*40)

