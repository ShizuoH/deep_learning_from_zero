# -*- conding: utf-8 -*-

# numpyによる行列演算の初期演習

import numpy as np

x = np.array([1, 2, 3])
print(x)
print(type(x))

y = np.array([2, 4, 6])
print(x + y)
print(x * y)
print(x / y)
print(2 * x)

A = np.array([[1, 2], [3, 4]])
print(A)
print(A.shape)
print(A.dtype)

A = np.array([[1, 2], [3, 4]])
B = A
B = B.flatten()
print(A)
print(B)

X = np.array([[51, 55], [14, 19], [0, 4]])
X = X.flatten()
Y = X[np.array([0, 2, 4])]
print(X)
print(Y)
print(X > 15)
print(X[X > 15])
