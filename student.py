import datetime

class Student:
    def __init__(self,student_id, name, age, grade, subjects):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.subjects = subjects
        self.enrolled_on = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "subjects": self.subjects,
            "enrolled_on": self.enrolled_on
        }

    @staticmethod
    def from_dict(data):

        student = Student(
            student_id=data["student_id"],
            name=data["name"],
            age=data["age"],
            grade=data["grade"],
            subjects=data["subjects"]
        )
        student.enrolled_on = data["enrolled_on"]

        return student

    def display(self):

        print("\n" + "~"*40)
        print(f"Student ID   : {self.student_id}")
        print(f"Name         : {self.name}")
        print(f"Age          : {self.age}")
        print(f"Grade        : {self.grade}")
        print(f"Subjects     : {', '.join(self.subjects)}")
        print(f"Enrolled on  : {self.enrolled_on}")
        print("~"*40)