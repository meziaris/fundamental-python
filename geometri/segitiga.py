from geometri.bangunruang import BangunRuang


class Segitiga(BangunRuang):
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi

    def info(self):
        return f'Ini adalah object Persegi Panjang dengan panjang = {self.alas}, dan lebar {self.tinggi}'

    def hitung_luas(self):
        return self.alas * self.tinggi / 2