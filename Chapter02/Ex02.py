n = int(input('Nhap so duong: '))

if n < 2:
    print('Khong phai so nguyen to')
else:
    nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            nguyen_to = False
            break
    if nguyen_to:
        print('La so nguyen to')
    else:
        print('Khong phai so nguyen to')