n = int(input('Nhap n: '))
tong = 0

while n > 0:
    tong += n % 10
    n //= 10

print('Tong cac chu so: ', tong)