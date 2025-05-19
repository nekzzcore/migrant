class Student:
    def init(self, name, gender, age, hair_color, eye_color):
        self.name = name
        self.gender = gender
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def str(self):
        return (f"Студент: {self.name}\\n"
                f"пол: {self.gender}\\n"
                f"возраст: {self.age}\\n"
                f"цвет волос: {self.hair_color}\\n"
                f"цвет глаз: {self.eye_color}\\n")

class GroupDatabase:
    def init(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        for student in self.students:
            print(student)

def main():
    db = GroupDatabase()

    # Example students
    db.add_student(Student("Студент1", "мужской", 20, "русый", "голубой"))
    db.add_student(Student("Студент2", "женский", 19, "черный", "карий"))
    db.add_student(Student("Студент3", "мужской", 21, "каштановый", "зеленый"))

    db.display_students()

if name == "main":
    main()