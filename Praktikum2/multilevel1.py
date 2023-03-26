# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Hewan:
    def __init__(self, spesies):
        self.spesies = spesies
    
    def makan(self):
        print("hewan sedang makan!!!")

class peliharaan(Hewan):
    def __init__(self, nama, spesies):
        super().__init__(spesies)
        self.nama = nama
    
    def bermain(self):
        print("hewan sdang bermain")
    
class cat(peliharaan):
    def __init__(self, nama, keturunan):
        super().__init__(nama, "angora")
        self.keturunan = keturunan
    
    def suara(self):
        print("meong meong")

Kucing = cat("moly", "angora")
print("spesies:", Kucing.spesies)
print("nama:", Kucing.nama)
Kucing.makan()
Kucing.bermain()
Kucing.suara()