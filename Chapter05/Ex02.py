import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 100)
y1 = x**2
y2 = x**3
plt.plot(x, y1, label='y = x^2')
plt.plot(x, y2, label='y = x^3')
plt.title('Do thi ham so')
plt.legend()
plt.show()