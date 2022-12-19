import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

#stacking matrix

c = np.hstack((a,b))
print(c)

d = np.vstack((a,b))
print(d)

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

cMat = np.hstack((aMat, bMat))
dMat = np.vstack((aMat, bMat))

print(cMat)
print(dMat)