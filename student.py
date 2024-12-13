from person import Person

class Student(Person):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.subjects = [] # Предметы студента
        self.grades = {} # Оценки студента

    # Получить список предметов студента
    def get_subjects(self):
        print(f'Студент {self.name} изучает предметы: {self.subjects}')

    # Получить оценки
    def get_grades(self):
        print(f'Оценки студента {self.name}: {self.grades}')