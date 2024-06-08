import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 200, size=100)
y = np.random.randint(0, 200, size=100)
colors = np.random.randint(0, 200, size=100)
sizes = np.random.randint(0, 200, size=100)
plt.scatter(x, y, s=sizes, c=colors)
plt.show()
