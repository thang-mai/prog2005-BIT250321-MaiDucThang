arr = list(map(int, input('Nhap danh sach: ').split()))

for x in arr:
    if x % 2 != 0:
        print(x, end=' ')