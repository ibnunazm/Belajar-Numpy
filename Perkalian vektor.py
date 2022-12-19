import numpy as np 
a = np.array([1,3,0])
b = np.array([2,1,0])

#perkalian dot
c = np.dot(a,b)
print(c)

a = np.array([1,3,0])
b = np.array([2,1,0])

#perkalian cross
c1 = np.cross(a, b)
print(c1)
c2 = np.cross(b, a)
print(c2)