arr = (list(map(int, input('Nhap danh sach: ').split())))

lon_nhat = nho_nhat = arr[0]

for x in arr:
    if x > lon_nhat:
        lon_nhat = x
    if x < nho_nhat:
        nho_nhat = x

print('So lon nhat: ', lon_nhat)
print('So nho nhat: ', nho_nhat)