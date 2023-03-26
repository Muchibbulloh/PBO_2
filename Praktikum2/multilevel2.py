# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Kendaraan:
    def __init__(self, warna, jenis):
        self.warna = warna
        self.jenis = jenis

class Mobil(Kendaraan):
    def __init__(self, warna, jenis, kecepatan):
        super().__init__(warna, jenis)
        self.kecepatan = kecepatan

    def berjalan(self):
        print(f"mobil berwarna {self.warna} di kendarai {self.kecepatan} km/h.")

class MobilListrik(Mobil):
    def __init__(self, warna, jenis, kecepatan, kapasitas_batre):
        super().__init__(warna, jenis, kecepatan)
        self.kapasitas_batre = kapasitas_batre

    def charge(self):
        print(f"mobil listrik berwarna {self.warna} sedang di charge dengan kapasitas batre {self.kapasitas_batre} kWh.")

my_electric_Mobil = MobilListrik("merah", 5, 120, 60)
my_electric_Mobil.berjalan()
my_electric_Mobil.charge()