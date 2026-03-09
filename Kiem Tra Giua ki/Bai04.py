def array():
    N = int(input("Nhap so phan tu cua mang: "))
    a = []
    for i in range(N):
        i = int(input())
        a.append(i)
    return a
array()

def selection_sort(a):
    for i in range(N):
        max_index = a[i]
    for j in range(i + 1, N):
        if a[j] > a[i]:
            max_index = a[j]
            a[i], a[max_index] = a[max_index], a[i]
            print(a)
    return a
selection_sort(a)
print("Mang sau khi sap xep:", a)