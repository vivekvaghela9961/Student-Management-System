import json
import os

from student import Student

DATA_FILE = "students_data.json"

def save_student(students):
    try:
        data = [students.to_dict() for students in students]
        with open(DATA_FILE, "w") as file:
            json.dump(data,file, indent=4)
        print("Students data saved Successfully✅")

    except Exception as e:
        print(e)

def load_student():

    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)

        students = [Student.from_dict(item) for item in data]
        return students

    except json.decoder.JSONDecodeError:
        print("⚠️ Data File is corrupted. Starting fresh.")
        return []

    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return []

def get_next_id(students):

    if not students:
        return 1
    return max(student.student_id for student in students) + 1