def Ham():
    a = input("Nhap so a:")
    b = input("Nhap so b:")
    c = input("Nhap so c:")
Ham()
def Sosanh():
    if a > b:
        if a > c:
            if b > c:
                print("So lon nhat la: ", a)
                print("So nho nhat la: ", c)
            else:
                print("So lon nhat la: ", a)
                print("So nho nhat la: ", b)
        else:
            print("So lon nhat la: ", c)
            print("So nho nhat la: ", b)
    elif a > c:
        print("So lon nhat la: ", b)
        print("So nho nhat la: ", c)
    elif b < c:
        print("So lon nhat la: ", c)
        print("So nho nhat la: ", a)
    else:
        print("So lon nhat la: ", b)
        print("So nho nhat la: ", a)
Sosanh()