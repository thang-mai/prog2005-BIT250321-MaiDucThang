def gt(a):
    if a == 0 or a == 1:
        return 1
    return a * gt(a - 1)

N = int(input('Nhap so can tinh: '))
print(f'Giai thua cua {N}: ', gt(N))