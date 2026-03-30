a = int(input('Nhap so thu nhat: '))
b = int(input('Nhap so thu hai: '))

while b != 0:
    a, b = b, a % b
print('UCLN = ', a)