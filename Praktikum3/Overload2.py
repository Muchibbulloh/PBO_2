# NAMA   : MUHAMAD MUCHIBBULLOH
# KELAS  : R2 ( B )
# NIM    : 210511078

class Ucapan:
    def suara(self):
        pass

class Pagi(Ucapan):
    def suara(self):
        return "Selamat Pagi"

class Siang(Ucapan):
    def suara(self):
        return "Selamat Siang"

class Sore(Ucapan):
    def suara(self):
        return "Selamat Sore"
    
class Malam(Ucapan):
    def suara(self):
        return "Selamat Malam"



daftar_ucapan = [Pagi(), Siang(), Sore(), Malam()]
for ucapan in daftar_ucapan:
    print(ucapan.suara())