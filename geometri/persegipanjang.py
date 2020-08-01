from geometri.bangunruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah object Persegi Panjang dengan panjang = {self.p}, dan lebar {self.l}'

    def hitung_luas(self):
        return self.p * self.l
