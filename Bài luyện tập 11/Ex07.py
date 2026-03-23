import csv

ten = input("Nhap ten: ")
tuoi = input("Nhap tuoi: ")
id_nv = input("Nhap id: ")
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"Ten: {ten}\n")
    f.write(f"Tuoi: {tuoi}\n")
    f.write(f"ID: {id_nv}\n")
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=";")
    writer.writerow(["Ten", "Tuoi", "ID"])
    writer.writerow([ten, tuoi, id_nv])
print("Da luu file!")
print("\nNoi dung file TXT:")
with open("nhanvien.txt", "r", encoding="utf-8") as f:
    print(f.read())
print("Noi dung file CSV:")
with open("nhanvien.csv", "r", encoding="utf-8") as f:
    print(f.read())