n = int(input('Nhap n: '))

if n < 2:
    print('Khong phai so nguyen to')
else:
    nt = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            nt = False
            break

    if nt:
        print('Day la so nguyen to')
    else:
        print('Khong pha so nguyen to')