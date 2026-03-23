def sap_xep_chon_theo_do_dai(arr):
    n = len(arr)
    for i in range(1, n):
        index = arr[i]
        j = i - 1
        while j >= 0 and len(arr[j]) < len(index):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = index
        print(f'Buoc {i}: {arr}')
arr1 = []
for i in range(5):
    s = input(f'Nhap chuoi thu {i + 1}: ')
    arr1.append(s)
print('Ban dau: ', arr1)
sap_xep_chon_theo_do_dai(arr1)
print('Sau khi xap xep:', arr1)