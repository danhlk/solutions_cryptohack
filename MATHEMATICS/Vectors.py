import numpy as np

v1 = [2, 6, 3]
w1 = [1, 0, 0]
u1 = [7, 7, 2]

v = np.array(v1)
w = np.array(w1)
u = np.array(u1)

print((2*u).dot(3*(2*v - w)))
