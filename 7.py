import pandas as pd
import matplotlib.pyplot as plt

data = {"Temp Day 1": [23, 26],
        "Temp Day 2": [24, 25],
        "Temp Day 3": [25, 26]}
x = pd.DataFrame(data, index=["LA", "NYC"])
x.plot(kind="bar")
plt.show()
