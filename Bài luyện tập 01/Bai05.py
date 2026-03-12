import random

M = int(input('Nhap so hang M: '))
N = int(input('Nhap so cot N: '))
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(1,101))
    matrix.append(row)
print("Ma tran: ")
for row in matrix:
    print(row)
cot = int(input('Nhap so cot muon hien thi: '))
if 1 <= cot <= N:
    print('Cot', cot, ':')
    for i in range(M):
        print(matrix[i][c-1])
else:
    print('Cot khong hop le')
max_value = matrix[0][0]
for i in range(M):
    for j in range(N):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
print('Phan tu lon nhat: ', max_value)