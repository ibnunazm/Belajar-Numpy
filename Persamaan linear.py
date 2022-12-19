import numpy as np 
A = np.array([(3,-2), 
              (10,2)])
print(A)
Y = np.array([12,14])

print(Y)

A_inv = np.linalg.inv(A)

X1 = np.dot(A_inv, Y)
print(X1)

X2 = np.linalg.solve(A, Y)
print(X2)