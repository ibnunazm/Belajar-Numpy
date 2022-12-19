import numpy as np

#Membuat matrix dengan tipe data tertentu
a = np.array(([1,2,3], [3,4,5]), dtype = float)
print(a)
a = np.array(([1,2,3], [3,4,5]), dtype = bool)
print(a)

#Membuat matrix dengan menggunakan function
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return kolom+baris

b = np.fromfunction(kuadrat, (1,10), dtype= int)
print(b)
c = np.fromfunction(jumlah, (5,5), dtype= int)
print(c)

#Membuat matrix dengan menggunakan iterasi
iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype = int)
print(d)

iterable = (x*2 for x in range(5))
e = np.fromiter(iterable, dtype = int)
print(e)

#multitype array
dtipe = [('nama', 'S255'), ('tinggi', int)]

data = [('ucup', 150),
        ('otong', 160),
        ('mario', 180)]

e = np.array(data, dtype=dtipe)

print(e[0])

