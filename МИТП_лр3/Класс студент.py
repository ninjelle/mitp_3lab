class Student:
    
    def __init__(self, name, age, student_id, major, grade=None):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.major = major
        self.grade = grade
    
    def display_info(self):
        print("=" * 40)
        print("ИНФОРМАЦИЯ О СТУДЕНТЕ")
        print("=" * 40)
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Студенческий ID: {self.student_id}")
        print(f"Специальность: {self.major}")
        if self.grade is not None:
            print(f"Средний балл: {self.grade:.2f}")
        else:
            print("Средний балл: не указан")
        print("=" * 40)
    
    def __str__(self):
        grade_info = f", средний балл: {self.grade:.2f}" if self.grade else ""
        return f"Студент {self.name} ({self.student_id}) - {self.major}{grade_info}"
    
    def update_grade(self, new_grade):
        if 0 <= new_grade <= 5:
            self.grade = new_grade
            print(f"Средний балл обновлен: {new_grade:.2f}")
        else:
            print("Ошибка: средний балл должен быть от 0 до 5")
