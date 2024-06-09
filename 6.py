from numpy import *
import matplotlib.pyplot as plt

x = linspace(-2 * pi, 2 * pi, 50)
y = sin(x)
plt.plot(x, y, label="sin")
y1 = cos(x)
plt.plot(x, y1, linestyle="-.", label="cos")
plt.legend()
plt.xlabel("Tetha", color="blue")
plt.ylabel("y", color="blue")
plt.show()
