import numpy as np 
import matplotlib.pyplot as plt

#garis
x = np.arange(0, 11, 1)
y = 2*x + 3
print(x)
print(y)

plt.figure(1)
plt.plot(x,y)

#lingkaran 
jari = 5
sudut = np.linspace(0, 2*np.pi, 100)
x2 = jari*np.cos(sudut)
y2 = jari*np.sin(sudut)
print(x2)
print(y2)


plt.figure(2)
plt.plot(x2,y2)

#segitiga
sisi = 5
sudut = np.linspace(0, 2*np.pi, 4)
x3 = sisi*np.cos(sudut)
y3 = sisi*np.sin(sudut)
print(x3)
print(y3)

plt.figure(3)
plt.plot(x3,y3)


#belah ketupat
sisi = 5
sudut = np.linspace(0, 2*np.pi, 5)
x4 = sisi*np.cos(sudut)
y4 = sisi*np.sin(sudut)
print(x4)
print(y4)


plt.figure(4)
plt.plot(x4,y4)
plt.show()
