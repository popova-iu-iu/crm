class Person():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f'Имя: {self.name}\nРоль: {self.role}'

    def get_name(self):
        print(f'{self.name}')

    def get_role(self):
        print(f'{self.role}')