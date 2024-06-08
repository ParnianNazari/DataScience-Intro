import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
y = np.array([25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25])
z = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
plt.scatter(x, y, c=z)
plt.colorbar()
plt.show()
