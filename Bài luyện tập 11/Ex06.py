n = int(input('Nhap so nguoi: '))
d = {}
for i in range(n):
    ten = input('Nhap ten: ')
    tuoi = int(input('Nhap tuoi: '))
    d[ten] = tuoi
tb = sum(d.values()) / len(d)
print('Tuoi trung binh: ', tb)
items = list(d.items())
for i in range(len(items)):
    max_indx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_indx][1]:
            max_indx = j
    items[i], items[max_indx] = items[max_indx], items[i]
print('Sau khi sap xep: ')
for ten, tuoi in items:
    print(ten, tuoi)