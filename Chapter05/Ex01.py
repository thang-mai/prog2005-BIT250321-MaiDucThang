import matplotlib.pyplot as plt
labels = ['Xuat sac', 'Gioi', 'Trung binh', 'Yeu', 'Kem']
values = [6, 10, 12, 4, 1]
plt.bar(labels, values)
plt.title('Ket qua hoc tap cua lop')
plt.xlabel('Xep loai')
plt.ylabel('So luong')
plt.show()