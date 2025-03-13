class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
        print(f"Hewan {self.nama} dari jenis {self.jenis} bersuara!")

kucing = Hewan("Milo", "Kucing")
kucing.bersuara()
