class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f'Ten hoa: {self.ten}, mau: {self.mau}'
ten = input('Nhap ten hoa: ')
mau = input('Nhap mau hoa: ')
hoa1 = Hoa(ten, mau)
print(hoa1)