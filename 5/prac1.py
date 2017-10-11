import numpy as np
import matplotlib.pyplot as plt

# 問題１
x = np.linspace(-np.pi, np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = y1 + y2
y4 = y1 * y2

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
plt.show()

