def thong_ke_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat
t = tuple(map(int,input('Nhap cac so nguyen cach nhau boi dau cach : ').split()))
tong, max_val, min_val = thong_ke_tuple(t)
print('Tong: ', tong)
print('Lon nhat: ', max_val)
print('Nho nhat: ', min_val)