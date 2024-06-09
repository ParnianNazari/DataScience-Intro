import numpy as np
import matplotlib.pyplot as plt
x = np.array([10, 20, 30, 40, 50])
y = np.array(["yellow","orange","grey","purple","pink"])
z = np.array(["a","b","c","d","e"])
plt.pie(x, colors=y, labels=z)
plt.show()