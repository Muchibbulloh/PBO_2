# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Mengajar:
    def mengajar(self):
        print("Mengajar")

class Inggris(Mengajar):
    def ygdiajar(self):
        print("Inggris")

class Indonesia(Mengajar):
    def ygdiajar2(self):
        print("Indonesia")

class Guru(Inggris, Indonesia):
    def pangkat(self):
        print("guru")

GuruA = Guru()
GuruA.mengajar()
GuruA.ygdiajar()
GuruA.ygdiajar2()
GuruA.pangkat()