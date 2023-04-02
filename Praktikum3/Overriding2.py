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


def panggil_suara(ucapan):
    print(ucapan.suara())

pagi = Pagi()
siang = Siang()
sore = Sore()
malam = Malam()

panggil_suara(pagi)
panggil_suara(siang)
panggil_suara(sore)
panggil_suara(malam)
