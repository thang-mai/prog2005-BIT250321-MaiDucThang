import os
import numpy as np
import matplotlib.pyplot as plt


#Bt1
def bai1():
    def lay_ten_file(path):
        return os.path.basename(path)

    def lay_ten_bai_hat(path):
        return os.path.splitext(os.path.basename(path))[0]

    path = input('Nhap duong dan: ')
    print('Ten file:', lay_ten_file(path))
    print('Ten bai hat:', lay_ten_bai_hat(path))


#Bt2
def bai2():
    s = input('Nhap chuoi: ')
    k = input('Nhap ky tu can dem: ')
    print('So lan xuat hien:', s.count(k))


#Bt3
def bai3():
    def giai_thua(n):
        if n <= 1:
            return 1
        return n * giai_thua(n-1)

    n = int(input('Nhap n: '))
    print('Giai thua =', giai_thua(n))


#Bt4
def bai4():
    s = input('Nhap chuoi: ')
    if s == '':
        print('Loi: Chuoi rong')
    else:
        print('Do dai chuoi:', len(s))


#Bt5
def bai5():
    x = np.linspace(0, 10, 100)

    plt.figure(figsize=(8,4))

    plt.subplot(1,2,1)
    plt.plot(x, x**2)
    plt.title('y = x^2')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.subplot(1,2,2)
    plt.plot(x, np.sqrt(x))
    plt.title('y = sqrt(x)')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.tight_layout()
    plt.show()


#Bt6
def bai6():
    s = input('Nhap chuoi: ')
    dao = ''
    for i in s:
        dao = i + dao
    print('Chuoi dao nguoc:', dao)


#Bt7
def bai7():
    while True:
        mk = input('Nhap mat khau: ')
        if mk == 'python123':
            print('Dung mat khau')
            break
        else:
            print('Sai, nhap lai')


#Bt8
def bai8():
    ds = [input('Nhap chuoi: ') for _ in range(5)]
    n = len(ds)

    for i in range(n):
        for j in range(0, n-i-1):
            if len(ds[j]) < len(ds[j+1]):
                ds[j], ds[j+1] = ds[j+1], ds[j]
                print('Buoc sap xep:', ds)

    print('Ket qua:', ds)


#Bt9
def bai9():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        # getter/setter name
        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            if value == '':
                raise ValueError('Ten khong hop le')
            self._name = value

        # getter/setter age
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


#Bt10
def bai10():
    ds = [input('Nhap chuoi: ') for _ in range(5)]
    n = len(ds)

    for i in range(n):
        for j in range(0, n-i-1):
            if len(ds[j]) < len(ds[j+1]):
                ds[j], ds[j+1] = ds[j+1], ds[j]
                print('Buoc sap xep:', ds)

    print('Ket qua:', ds)


#Bai11
while True:
    print('\nMENU BAI TAP')
    print('1. Bai 1')
    print('2. Bai 2')
    print('3. Bai 3')
    print('4. Bai 4')
    print('5. Bai 5')
    print('6. Bai 6')
    print('7. Bai 7')
    print('8. Bai 8')
    print('9. Bai 9')
    print('10. Bai 10')
    print('0. Thoat')

    chon = input('Chon bai: ')

    if chon == '1':
        bai1()
    elif chon == '2':
        bai2()
    elif chon == '3':
        bai3()
    elif chon == '4':
        bai4()
    elif chon == '5':
        bai5()
    elif chon == '6':
        bai6()
    elif chon == '7':
        bai7()
    elif chon == '8':
        bai8()
    elif chon == '9':
        bai9()
    elif chon == '10':
        bai10()
    elif chon == '0':
        break
    else:
        print('Lua chon khong hop le')