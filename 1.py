import numpy as np
import matplotlib.pyplot as plt

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
y = np.array([25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25])
plt.plot(x, y, label="Data 1")

x1 = np.array([-4, -1, 2, 5])
y1 = np.array([-4, -1, 2, 5])
plt.plot(x1, y1, label="Data 2")
plt.legend()
plt.xlabel("x", color="red")
plt.ylabel("y", color="red")
plt.title("xy plot", color="red")
plt.show()
