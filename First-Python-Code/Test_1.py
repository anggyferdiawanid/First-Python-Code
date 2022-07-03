"""
program perulangan
"""

DaftarBuku = ['Rich Dad poor Dad' , 'Seven Habits' , 'Cashflow Quadrant' , 'The Power Of Kepepet']
print(DaftarBuku)

for buku in DaftarBuku:
    print(buku)

print('\nDaftar Bukunya adalah:')
print(DaftarBuku[0])
print(DaftarBuku[3])

print('\nTampilkan dengan in Range')
for i in range(0, len(DaftarBuku)):
    print(DaftarBuku[i])

print('\nDaftar Bukunya')
DaftarBuku = ['Rich Dad poor Dad' , 'Seven Habits' , 'Cashflow Quadrant' , 'The Power Of Kepepet']

print('\nTambahan buku bacaan')
DaftarBuku.append('Zillenials')

for i in range(0, len(DaftarBuku)):
    print(DaftarBuku[i])

print('\nGanti buku yang pertama')
DaftarBuku = ['Rich Dad poor Dad' , 'Seven Habits' , 'Cashflow Quadrant' , 'The Power Of Kepepet']
DaftarBuku[0]  = 'Bahasa Indonesia kelas 12 SMK'
for i in range(0, len(DaftarBuku)):
    print(DaftarBuku[i])
    
print('\nBuku keduamu dipijam Ameer nih')
DaftarBuku = ['Rich Dad poor Dad' , 'Seven Habits' , 'Cashflow Quadrant' , 'The Power Of Kepepet']
buku = DaftarBuku.pop(1)
for i in range(0, len(DaftarBuku)):
    print(DaftarBuku[i])

print('\nBuku yang dipinjam adalah:')
print(buku)