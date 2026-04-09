def sapxep(a):
    n = len(a)
    dem = 0
    for i in range(n):
        for j in range(n - i -1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                dem += 1
    print('So buoc: ', dem)
    return a

arr = list(map(int, input('Nhap day so: ').split()))
print('Day sau khi sap xep: ', sapxep(arr))