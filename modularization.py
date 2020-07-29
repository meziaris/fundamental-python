"""
Program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""
from geometri.luaspersegipanjang import luas_persegi_panjang

alas = 10
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Segitiga dengan alas={alas} dan tinggi={tinggi}, memiliki luas {luas_segitiga}')

print('\nLuas segitiga dengan fungsi')
def menghitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'Luas segitiga dengan alas 6 dan tinggi 3, adalah {menghitung_luas_segitiga(6, 3)}')
print(f'Luas segitiga dengan alas 10 dan tinggi 4, adalah {menghitung_luas_segitiga(10, 4)}')
print(f'Luas segitiga dengan alas 20.2 dan tinggi 7.5, adalah {menghitung_luas_segitiga(20.2, 7.5)}')

print('\nMenggunakan package (package geometri dan modul luaspersegipanjang)')
print(f'Luas persegi panjang, panjang 10 dan lebar 6 adalah {luas_persegi_panjang(10, 6)}')