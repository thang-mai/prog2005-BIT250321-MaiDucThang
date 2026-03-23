a = [1, 3, 5 ,7, 9]
print('Danh sach ban dau: ', a)
x = int(input('Nhap phan tu them vao: '))
a.append(x)
print('Danh sach sau khi them: ', a)
k = int(input('Nhap phan tu can kiem tra: '))
print('So lan xuat hien: ', a.count(k))
def so_nguyen_to(n):
    if n < 2:
        return False
    for i in range (2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
tong = sum(i for i in a if so_nguyen_to(i))
print('Tong so nguyen to: ', tong)
a.sort()
print('Sau khi sap xep: ', a)
a.clear()
print('Danh sach sau khi xoa: ', a)