# NAMA   : MUHAMAD MUCHIBBULLOH
# KELAS  : R2 ( B )
# NIM    : 210511078

class Hewan:
    def suara(self):
        pass

class Serigala(Hewan):
    def suara(self):
        return "Auuuuuuu"

class Singa(Hewan):
    def suara(self):
        return "Arrggghhhhh"

class Sapi(Hewan):
    def suara(self):
        return "Moo"
    
class Domba(Hewan):
    def suara(self):
        return "Mbeee"



daftar_hewan = [Serigala(), Singa(), Sapi(), Domba()]
for hewan in daftar_hewan:
    print(hewan.suara())