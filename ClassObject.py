class Mobil:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.kecepatan = 0

    def nyalakan_mesin(self):
        print(f"Mesin {self.merk} {self.model} dinyalakan.")

    def tambah_kecepatan(self, nilai):
        self.kecepatan += nilai
        print(f"Kecepatan bertambah {nilai} km/jam. Kecepatan sekarang: {self.kecepatan} km/jam.")

    def rem(self, nilai):
        self.kecepatan -= nilai
        if self.kecepatan < 0:
            self.kecepatan = 0
        print(f"Rem ditekan, kecepatan berkurang {nilai} km/jam. Kecepatan sekarang: {self.kecepatan} km/jam.")

# Contoh penggunaan
mobil1 = Mobil("Toyota", "Corolla", 2022)
mobil1.nyalakan_mesin()
mobil1.tambah_kecepatan(30)
mobil1.rem(10)
