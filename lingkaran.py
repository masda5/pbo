import math

class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return math.pi * self.jari_jari ** 2

blt = Lingkaran(7)
print(f"Luas lingkaran: {blt.hitung_luas():.2f}")
