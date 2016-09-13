import numpy as np

x = np.arange(10)
y = x**2

for i in range(len(x)):
    print('{0:3.0f} {1:3.0f}'.format(x[i], y[i]))
