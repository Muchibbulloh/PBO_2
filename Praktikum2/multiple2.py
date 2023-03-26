# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Manusia:
    def __init__(self, nama ,umur):
        self.nama = nama
        self.umur = umur
        
class Penari:
    def __init__(self, tempat):
        self.tempat = tempat
        
class Murid (Manusia, Penari):
    def __init__(self, nama, umur, tempat):
        Manusia.__init__(self, nama, umur)
        Penari.__init__(self,tempat)
        
ujang = Murid( 'Mawang', 20, 'teater')
print (ujang.nama)
print (ujang.umur)
print (ujang.tempat) 