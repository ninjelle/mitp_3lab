class Student:
    
    def __init__(self, name, age, student_id, major, grade=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.grade = grade
    
    def display_info(self):
        print("=" * 40)
        print("Student information")
        print("=" * 40)
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Major: {self.major}")
        if self.grade is not None:
            print(f"Grade: {self.grade:.2f}")
        else:
            print("Grade: not specified")
        print("=" * 40)
    
    def __str__(self):
        grade_info = f", Grade: {self.grade:.2f}" if self.grade else ""
        return f"\nStudent {self.name} ({self.student_id}) - {self.major}{grade_info}\n"

    @staticmethod
    def get_student_by_id(students_list, student_id):
        for student in students_list:
            if student.student_id == student_id:
                return student
        return None

if __name__ == "__main__":
        student1 = Student("Zvereva Ekaterina Konstantinovna", 20, "ST2024001", "Software engineering", 4.5)
        student2 = Student("Tumanyan Lina Vrezhovna", 19, "ST2024002", "Software engineering")
        student3 = Student("Simbireva Anastasia Alekseevna", 21, "ST2024003", "Software engineering", 4.8)
    
        student1.display_info()

    
        print("Students list:")
        students = [student1, student2, student3]
        for i, student in enumerate(students, 1):
            print(f"{i}. {student}")
   
        print(student2)

        found_student = Student.get_student_by_id(students, "ST2024002")
        if found_student:
            print(f"Found student: {found_student.name}")
            found_student.display_info()
        else:
            print("Student not found")