a = []

for i in range(5):
    b = input(f'Nhap ten nguoi thu {i + 1}: ')
    a.append(b)
    print('Danh sach hien tai gom: ', a)
a.pop(1)

print('Danh sach sau khi xoa: ', a)