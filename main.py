from bs4 import BeautifulSoup
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import Segitiga
import requests

p1 = PersegiPanjang(4, 6)
print(p1.info())
print(f'Luasnya adalah {p1.hitung_luas()}')

s1 = Segitiga(6, 3)
print(f'\n{s1.info()}')
print(f'Luasnya adalah {s1.hitung_luas()}')

# Polymerphism
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)

print('\nPolymerphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())

print('\nMenggunakan package BeautifulSoup4')
url = 'https://mezi.space'
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f'Success! Response Code = {response.status_code}')
        soup = BeautifulSoup(response.text, features="html.parser")
        print(f'Title: {soup.title.string}')
        print(f'Isi {url} adalah (dalam tag p):')
        print(soup.p.get_text())
except Exception as e:
    print(f'There is an error {e}')