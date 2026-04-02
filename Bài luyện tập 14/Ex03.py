n = int(input('Nhap so n: '))

#hinh 1
for i in range(n):
    for j in range(n):
        print('1', end='  ')
    print()

print('\n')

#hinh 2
for i in range(n):
    for j in range(n):
        print(j + 1, end='  ')
    print()

print('\n')

#hinh 3
for i in range(n):
    for j in range(i + 1):
        print(j + 1, end='  ')
    print()

print('\n')

#hinh 4
for i in range(n):
    for j in range(n - i):
        print(j + 1, end='  ')
    print()

print('\n')

#hinh 5
for i in range(n):
    for j in range(n):
        if j == 0 or i == n - 1 or j == i:
            print(j + 1, end='  ')
        else:
            print(' ', end='  ')
    print()

print('\n')

#hinh 6
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - i - 1:
            print(j + 1, end='  ')
        else:
            print(' ', end='  ')
    print()

print('\n')

#hinh 7
for i in range(n + 1):
    for j in range(n - i):
        print(' ', end='  ')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(' ',end='  ')
        else:
            print(i, end='  ')
    print()

print('\n')

#hinh 8
for i in range(1, n + 1):
    print("   " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end="  ")
    for j in range(i - 1, 0, -1):
        print(j, end="  ")
    print()

print('\n')

#hinh 9
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    if i < n:
        print("1", end="")
        print("  " * (2 * i - 3), end="  ")
        if i > 1:
            print("1", end="")
    else:
        for j in range(1, n + 1):
            print(j, end=" ")
        for j in range(n - 1, 0, -1):
            print(j, end=" ")
    print()