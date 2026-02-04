class Student:
    def __init__(self, name, group, average_grade):
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def show_info(self):
        print(f"Студент: {self.name} | Група: {self.group} | Середній бал: {self.average_grade}")

student1 = Student("Олексій", "КН-11", 4.8)
student2 = Student("Анна", "ІП-12", 5.0)
student3 = Student("Максим", "КН-11", 3.9)

student1.show_info()
student2.show_info()
student3.show_info()