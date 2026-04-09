class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Ten khong hop le')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value <= 0:
            raise ValueError('Tuoi phai lon hon 0')
        self._age = value

    def greet(self):
        return 'Hello'

    @classmethod
    def species(cls):
        return 'Human'

    @staticmethod
    def info():
        return 'Thong tin chung'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __str__(self):
        return f'{self.name} - {self.age}'

class Student(Person):
    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value < 0 or value > 10:
            raise ValueError('Diem phai tu 0 den 10')
        self._score = value

    def __str__(self):
        return f'{self.name} - {self.age} - {self.score}'


s1 = Student('An', 20, 8)
s2 = Student('An', 20, 8)

print(s1)
print(s1.name)
print(s1.age)
print(s1.score)
print(s1.greet())
print(Student.species())
print(Student.info())
print('So sanh:', s1 == s2)