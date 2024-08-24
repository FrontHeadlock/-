import numpy as np
import matplotlib.pyplot as plt

'''X = np.arange(0, 6, 0.1)
Y = np.sin(X)

plt.plot(X,Y)
plt.show()'''

x=np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x, y1, label ="sin")
plt.plot(x, y2, linestyle = "--", label = "cos")
plt.xlabel("X")
plt.ylabel("Y")
plt.title('sin & cos')
plt.legend()
plt.show()

