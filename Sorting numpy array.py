import numpy as np

a = np.floor(np.random.randn(1,6)*10)
print(a)

print('nilai maksimum dari a = ', a.max())
print('posisi dari nilai maksimum = ', a.argmax())

print('nilai minimum dari a = ', a.min())
print('posisi dari nilai minimum = ', a.argmin())

print('mengurutkan nilai a : ')
print(np.sort(a))
print(np.argsort(a))

a = np.floor(np.random.randn(2,2)*10)
print(a)

print('nilai maksimum dari a = ', a.max())
print('posisi dari nilai maksimum = ', a.argmax())

print('nilai minimum dari a = ', a.min())
print('posisi dari nilai minimum = ', a.argmin())

print('mengurutkan nilai a : ')
print(np.sort(a))
print(np.argsort(a))

dtipe = [('nama', 'S10'), ('tinggi', int)]
data = [('ucup', 170),
        ('otong', 150),
        ('mario', 180)]

a = np.array(data, dtype = dtipe)
print(a)

print(np.sort(a, order='tinggi'))
print(np.sort(a, order='nama'))