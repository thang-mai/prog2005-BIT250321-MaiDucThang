import matplotlib.pyplot as plt
cities = ['LA', 'San Diego', 'San Jose', 'SF', 'Fresno', 'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim']
areas = [1302, 964, 467, 121, 297, 259, 133, 202, 389, 131]
data = list(zip(cities, areas))
data.sort(key=lambda x: x[1], reverse=True)
cities_sorted, areas_sorted = zip(*data)
plt.barh(cities_sorted, areas_sorted)
plt.title('Top 10 thanh pho theo dien tich(California)')
plt.xlabel('Dien tich (km2)')
plt.ylabel('Thanh pho')
plt.show()