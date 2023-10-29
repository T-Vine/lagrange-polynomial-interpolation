import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)

y = x**2 + 2*x + 2

fig, ax = plt.subplots()
ax.plot(x,y)