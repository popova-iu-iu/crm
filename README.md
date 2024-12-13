Создаем студентов
s1 = Student('Мишка Сберкнижка', 'Студент')
s2 = Student('Вася Пупкин', 'Студент')

Создаем учителей
t1 = Teacher('Михаил', 'Преподаватель', 'История')
t2 = Teacher('Олег', 'Преподаватель', 'Английский язык')

Учителя добавляют студентов на свои предметы
t1.add_student(s1)
t1.add_student(s2)
t2.add_student(s1)

Учителя ставят оценки студентам
t1.rate_student(s1, 5)
t1.rate_student(s2, 4)
t2.rate_student(s1, 3)

Выводим данные журнала учителей
t1.get_journal_data()
t2.get_journal_data()

Удаляем студента с предмета
t1.remove_student(s2)
