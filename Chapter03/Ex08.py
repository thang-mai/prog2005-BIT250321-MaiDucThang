arr = list(map(float, input('Nhap danh sach: ').split()))

for x in arr:
    if x > 10:
        print(x)
        break
    else:
        print('Khong co so lon hon 10')