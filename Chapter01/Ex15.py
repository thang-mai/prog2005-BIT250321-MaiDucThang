students = []

for i in range(3):
    name = input("Nhap ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))

    avg = (toan + ly + hoa) / 3
    students.append((name, avg))

print("\nKet qua:")
for name, avg in students:
    print(name, "-", round(avg, 2))