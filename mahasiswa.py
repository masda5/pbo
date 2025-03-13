class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def cetak_krs(self):
        print(f"Mahasiswa {self.nama} dengan NIM {self.nim} mencetak KRS.")

mhs = Mahasiswa("Masda", "230705136")
mhs.cetak_krs()
