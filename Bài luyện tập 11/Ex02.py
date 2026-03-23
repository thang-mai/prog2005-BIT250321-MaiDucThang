def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            right = mid - 1
        else:
            left = mid + 1

    return -1

a = []
for i in range(5):
    a.append(input(f"Nhap chuoi {i+1}: "))

a.sort(reverse=True)

x = input("Nhap chuoi can tim: ")

kq = binary_search(a, x)

if kq != -1:
    print("Tim thay tai vi tri:", kq)
else:
    print("Khong tim thay")