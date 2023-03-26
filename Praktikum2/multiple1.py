# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Pasien:
    def __init__(self, nama, nik):
        self.nama = nama
        self.nik = nik
    def dicek(self):
        print(self.nama, "sedang dicek")
class Pekerja:
    def __init__(self, nama, pekerjaan):
        self.nama = nama
        self.pekerjaan = pekerjaan
    def pekerja(self):
        print(self.nama, "seorang pekerja")
class PasienPekerja(Pasien, Pekerja):
    def __init__(self, nama, nik, pekerjaan):
        Pasien.__init__(self, nama, nik)
        Pekerja.__init__(self, nama, pekerjaan)
    def bersosialisasi(self):
        print(self.nama, "sedang cek darah")
mhs_pekerja = PasienPekerja("Maskulin", "190001", "kasir")
mhs_pekerja.dicek()
mhs_pekerja.pekerja()
mhs_pekerja.bersosialisasi() 