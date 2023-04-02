# NAMA   : MUHAMAD MUCHIBBULLOH
# KELAS  : R2 ( B )
# NIM    : 210511078

class Hewan:
    def suara(self):
        pass

class Serigala(Hewan):
    def suara(self):
        return "Auuuuuuuuu"

class Singa(Hewan):
    def suara(self):
        return "Arghhhhhhhhh"

class Sapi(Hewan):
    def suara(self):
        return "Moo"

class Domba(Hewan):
    def suara(self):
        return "Mbeee"

def panggil_suara(hewan):
    print(hewan.suara())

Serigala = Serigala()
Singa = Singa()
sapi = Sapi()
domba = Domba()

panggil_suara(Serigala)
panggil_suara(Singa)
panggil_suara(sapi)
panggil_suara(domba)