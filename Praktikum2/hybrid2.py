# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Hewan:
    def __init__(self, nama):
        self.nama = nama
    
    def suara(self):
        pass
    
class Serigala(Hewan):
    def suara(self):
        return "Auuuuuu!!"
    
class Kucing(Hewan):
    def suara(self):
        return "Meong!!"
    
class Burung(Hewan):
    def suara(self):
        return "cittt ciit!!"
    
def main():
    serigala = Serigala("Buddy")
    kucing = Kucing("Mittens")
    burung = Burung("Polly")
    
    print(serigala.nama + ": " + serigala.suara())
    print(kucing.nama + ": " + kucing.suara())
    print(burung.nama + ": " + burung.suara())

if __name__ == "__main__":
    main()