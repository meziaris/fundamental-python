print('Hello world!')
print('by meziaris')
print('-' * 10)

# if else
print('\nIf Else')
ingin_cepat = True
if ingin_cepat:
    print('Jalan lurus ya!')
else:
    print('Jalan lain')

# looping
print('\nLooping')
jumlah_anak = 4
for index_anak in range(1, jumlah_anak + 1):
    print(f'Halo anak ke #{index_anak}')

# data type
print('\nTipe data skalar - tipe data sederhana')
anak1 = 'Mezi'
anak2 = 'Nano'
anak3 = 'Neni'
anak4 = 'Nunu'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

print('\nTipe data list/daftar/array')
anak = ['Mezi', 'Nano', 'Neni', 'Nunu']
print(anak)

print('\nTambah satu anak')
anak.append('Nanang')
print(anak)

print('\nSapa anak ke 2')
print(anak[1])

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak : cara ribet')
for a in range(0, len(anak)):
    print(f'{a + 1}. Hai {anak[a]}!')

"""
Data Type Dict
Tipe data dictionary sekedar menghubungkan KEY dan VALUE
KVP = Key Value Pair
"""
print('\nData type dict')
kamus_ind_eng = {'anak': 'son', 'ibu': 'mother', 'ayah': 'father'}
print(kamus_ind_eng)
print(kamus_ind_eng['ibu'])
print(kamus_ind_eng['ayah'])
