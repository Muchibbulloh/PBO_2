# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Smartphone:
    def __init__(self, nama, type):
     self.nama = nama
     self.type = type
    def bertype(self):
        print(self.nama, "Samsung")
class Android(Smartphone):
    def __init__(self, nama, type, garansi):
     super().__init__(nama, type)
     self.garansi = garansi
    def bergaransi(self):
     print(self.garansi,"2 tahun")
kucingA = Android("HP", 2, "Bergaransi")
kucingA.bertype() 
kucingA.bergaransi() 