'''
def sx(a):
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

b = []
c = int(input('Nhap so phan tu cua day: '))
for i in range(c):
    d = float(input(f'So thu {i + 1}: '))
    b.append(d)

print('Day so sau khi sap xep: ', sx(b))
'''

a = list(map(float, input('Nhap day: ').split()))

n = len(a)

for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print('Day so sau khi sap xep: ', a)