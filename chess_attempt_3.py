import numpy as np

x = np.zeros((8,8))
x[1::2] = 5
print(x)