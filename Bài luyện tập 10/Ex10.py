ds = []
for i in range(5):
    ds.append(input(f'Nhap chuoi thu {i + 1}: '))

n = len(ds)

for i in range(n):
    for j in range(0, n-i-1):
        if len(ds[j]) < len(ds[j+1]):
            ds[j], ds[j+1] = ds[j+1], ds[j]
            print('Buoc: ', ds)

print('Ket qua: ', ds)