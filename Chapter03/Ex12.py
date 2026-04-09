m = int(input('Nhap so dong: '))
n = int(input('Nhap so cot: '))

A = []
print('Nhap ma tran A: ')
for i in range(m):
    a = (list(map(int, input().split())))
    A.append(a)

B = []
print('Nhap ma tran B: ')
for i in range(m):
    b = (list(map(int, input().split())))
    B.append(b)

C = []

for i in range(m):
    hang = []
    for j in range(n):
        hang.append(A[i][j] + B[i][j])
    C.append(hang)

print('Ma tran tong: ')
for hang in C:
    for x in hang:
        print(x, end=' ')
    print()