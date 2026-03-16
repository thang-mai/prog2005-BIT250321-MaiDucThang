def bmi():
    kg = float(input('Nhap can nang: '))
    m = float(input('Nhap chieu cap: '))
    bmi = kg / (m*m)
    print('BMI = ', round(bmi, 2))
bmi()