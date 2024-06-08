import numpy as np
import matplotlib.pyplot as plt
x = np.array(["Chicago", "Los Angeles", "New York"])
y = np.array([2664452, 3820914, 8258035])
z = np.array(["violet", "orchid", "purple"])
plt.bar(x, y, color=z)
plt.xlabel("Cities", color="blue")
plt.ylabel("Population Estimation", color="blue")
plt.show()

