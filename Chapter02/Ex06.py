def gt(n):
    if n == 0 or n == 1:
        return 1
    return n * gt(n-1)

n = int(input('Nhap so duong: '))
print(f'Giai thua cua {n}: ', gt(n))