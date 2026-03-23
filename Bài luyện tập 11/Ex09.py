m = int(input('Nhap so dong: '))
n = int(input('Nhap so cot: '))
A = []
B = []
print('Nhap ma tran A')
for i in range(m):
    row = []
    for j in range(n):
        x = input(f'A[{i}][{j}] = ')
        if x == '':
            print('Loi: khong duoc de trong')
            exit()
        row.append(x)
    A.append(row)
print('Nhap ma tran B')
for i in range(m):
    row = []
    for j in range(n):
        x = input(f'B[{i}][{j}] = ')
        if x == '':
            print('Loi: khong duoc de trong')
            exit()
        row.append(x)
    B.append(row)
C = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(A[i][j] + B[i][j])
        C.append(row)
print('Ma tran tong: ')
for row in C:
    print(row)
