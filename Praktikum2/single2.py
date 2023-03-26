# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Laptop:
    def __init__(self, nama,type ):
     self.nama = nama
     self.type = type
    def berharga(self):
        print(self.nama, "harga 5jt")
class Windows(Laptop):
    def __init__(self, nama, type, jenis_OS):
     super().__init__(nama, type)
     self.jenis_OS = jenis_OS
    def bergaransi(self):
     print("garansi 1 tahun")
kucingA = Windows("Asus", 2, "Baru")
kucingA.berharga() 
kucingA.bergaransi() 