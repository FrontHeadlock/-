import numpy as np
import matplotlib.pyplot as plt

def leaky_relu(x, alpha = 0.2):
    return np.maximum(x,alpha*x)

x= np.arange(-2.0, 2.0, 0.01)
y=leaky_relu(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Leaky ReLU, alpha=0.2')
plt.title('Leaky ReLU Function with np.arrange')
plt.xlabel('Input (x)')
plt.ylabel('Output (y)')
plt.legend()
plt.grid(True)
plt.show()
