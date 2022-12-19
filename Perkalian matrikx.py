import numpy as np

a = np.array([(1,2,5),
              (3,4,6)])
b = np.ones([3,1])

print('matrik a : \n', a)
print('matrik b : \n', b)

#perkalian matrix
c1 = np.dot(a, b)
print('matrik c1 : \n', c1)

c2 = a.dot(b)
print('matrik c2 : \n', c2)