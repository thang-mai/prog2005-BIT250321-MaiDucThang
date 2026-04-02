n = int(input('Nhap so n: '))

#hinh 1
for i in range(n):
    for j in range(n):
        print('*', end='  ')
    print()

print('\n')

#hinh 2
for i in range(n):
    for j in range(i + 1):
        print('*', end='  ')
    print()

print('\n')

#hinh 3
for i in range(n):
    for j in range(n - i):
        print('*', end='  ')
    print()

print('\n')

#hinh 4
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='  ')
    for j in range(i + 1):
        print('*', end='  ')
    print()

print('\n')

#hinh 5
for i in range(n):
    for j in range(n):
        if j == 0  or i == n - 1 or j == i:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()

print('\n')

#hinh 6
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - i - 1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()

print('\n')

#hinh 7
for i in range(n):
    for j in range(n):
        if i == n - 1 or j == n - 1 or j == n - i - 1:
            print('*', end='  ')
        else:
            print(' ', end='  ')
    print()

print('\n')

#hinh 8
for i in range(n + 1):
    for j in range(n - i):
        print(' ', end='  ')
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print(' ',end='  ')
        else:
            print('*', end='  ')
    print()

print('\n')

#hinh 9
for i in range(n):
    print(" " * (n - i - 1), end="")
    if i == 0:
        print("*")
    elif i == n - 1:
        print("* " * n)
    else:
        print("*" + " " * (2 * i - 1) + "*")

print('\n')

#hinh 10
for i in range(n):
    print(" " * i, end="")
    if i == 0:
        print("* " * n)
    elif i == n - 1:
        print("*")
    else:
        print("*" + " " * (2 * (n - i - 1) - 1) + "*")