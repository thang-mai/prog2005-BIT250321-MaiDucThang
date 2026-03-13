def diem_tb(ds):
    tong = sum(ds.values())
    so_sv = len(ds)
    return tong / so_sv
sv = {}
n = int(input('Nhap so sinh vien: '))
for i in range(n):
    ten  = input('Nhap ten sinh vien: ')
    diem = float(input('Diem: '))
    sv[ten] = diem
tb = diem_tb(sv)
print('Diem trung binh: ', tb)