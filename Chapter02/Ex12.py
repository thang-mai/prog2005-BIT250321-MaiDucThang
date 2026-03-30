n = int(input('Nhap n: '))
tong = 0

for i in range(1, n+1):
    if i % 2 != 0:
        tong += i
print(f'Tong so le tu 1 den {n}: ',tong)