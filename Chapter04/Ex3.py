data = {}
n = int(input('Nhap so phan tu: '))
for i in range(n):
    key = input('Nhap key: ')
    value = input('Nhap value: ')
    data[key] = value
k = input('Nhap key can kiem tra: ')
if k in data:
    print('Ton tai')
else:
    print('Khong ton tai')