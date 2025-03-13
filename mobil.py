class Mobil:
    def __init__(self, merk, warna):
        self.merk = merk
        self.warna = warna

    def nyalakan_mesin(self):
        print(f"Mobil {self.merk} berwarna {self.warna} telah dinyalakan.")

avanza = Mobil("Toyota Avanza", "Hitam")
avanza.nyalakan_mesin()
