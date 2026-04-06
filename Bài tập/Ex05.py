a = list(map(int, input('Nhap danh sach: ').split()))

def ngto(n):
    if n < 2:
        return False
    for i in range(2, int(n**0,5) + 1):
        if n % i == 0:
            return False
    return True

so_le= [x for x in a if x % 2 != 0]
so_nguyen_to = [x for x in a if ngto(x)]

print(f'Co {len(so_le)} so le, Cac so le: ', so_le)
print('Cac so nguyen to: ', so_nguyen_to)