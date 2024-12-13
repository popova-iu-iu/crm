from person import Person
from student import Student

class Teacher(Person):
    def __init__(self, name, role, subject):
        super().__init__( name, role)
        self.subject = subject
        self.journal = {}

    # Добавить студента на курс
    def add_student(self, student):
        if student.name not in self.journal:
            self.journal[student.name] = []
            if isinstance(student, Student):
                student.subjects.append(self.subject)
                student.grades[self.subject] = []
            print(f'Студент {student.name} записан на предмет: {self.subject}')
        else:
            print(f'Студент уже посещает предмет: {self.subject}')

    # Отчислить студента с курса
    def remove_student(self, student):
        if student.name in self.journal:
            del self.journal[student.name]
            if isinstance(student, Student):
                student.subjects.remove(self.subject)
                del student.grades[self.subject]
            print(f'Студент {student.name} отчислен с предмета {self.subject}')
        else:
            print(f'Студент {student.name} отсутствует в журнале предмета {self.subject}')

    # Получить данные журнала
    def get_journal_data(self):
        print(self.journal)

    # Поставить оценку студенту
    def rate_student(self, student, mark):
        if student.name in self.journal:
            self.journal[student.name].append(mark)
            if isinstance(student, Student):
                student.grades[self.subject].append(mark)
            print(f'Студент {student.name} получил оценку {mark} по предмету {self.subject}')
        else:
            print(f'Студент {student.name} отсутствует в журнале предмета {self.subject}')

    # Посчитать средний балл студента
    def get_summary_rate(self, student):
        if student.name in self.journal:
            summary_rate = sum(self.journal[student.name])/len(self.journal[student.name])
            print(f'Средний балл студента {student.name} по предмету {self.subject}: {summary_rate}')
        else:
            print(f'Студент {student.name} отсутствует в журнале предмета {self.subject}')