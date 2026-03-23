n = int(input('Nhap so luong phan tu: '))
a = []
for i in range(n):
    a.append(int(input(f'Nhap so thu {i+1}: ')))
tong = 0
print('Cac so chan: ')
for x in a:
    if x % 2 == 0:
        print(x, end=' ')
        tong += x
print('\nTong cac so chan: ', tong)