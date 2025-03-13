class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

kotak = Persegi(5)
print(f"Luas persegi: {kotak.hitung_luas()}")
