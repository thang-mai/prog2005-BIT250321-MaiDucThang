#Cach 1

s = input('Nhap chuoi: ')
print('Chuoi dao nguoc: ', s[::-1])

#Cach 2

s = input('Nhap chuoi: ')
a = ''
for x in s:
    a = x + a

print('Chuoi dao nguoc: ', a)