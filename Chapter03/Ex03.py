mau = ['Red', 'Green', 'Blue', 'yellow', 'white']

try:
    mau.remove('Green')
except ValueError:
    print('Khong co Green trong danh sach')

print('Danh sach: ', mau)