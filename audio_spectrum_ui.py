import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 200)
y = np.sin(x/8) * np.exp(-x/80)
plt.plot(x, y)
plt.title("spectrum decay")
plt.savefig("spectrum_demo.png")
