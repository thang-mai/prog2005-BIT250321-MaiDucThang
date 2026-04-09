arr = (list(map(float, input('Nhap danh sach: ').split())))
tong = 0

for x in arr:
    if x % 2 == 0:
        tong += x
        print(x, end=' ')

print('\nTong cac so chan: ', tong)