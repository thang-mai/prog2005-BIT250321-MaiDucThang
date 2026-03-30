def tong(n):
    if n == 1:
        return 1
    return n + tong(n-1)

n = int(input('Nhap n: '))
print('Tong = ', tong(n))