def count_vowels(s):
    count = 0
    vowels = 'aeiuo'
    for c in s.lower():
        if c in vowels:
            count += 1
    return count

s = input('Nhap chuoi: ')
print('So nguyen am: ', count_vowels(s))