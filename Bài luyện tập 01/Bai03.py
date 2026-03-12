a = int(input('Nhap 1 so trong khoang tu 1 den 9: '))
if a < 1 or a > 9:
    print('So nhap khong hop le')
else:
    for i in range(1,10):
        print(a, 'x', i, '=', a*i)