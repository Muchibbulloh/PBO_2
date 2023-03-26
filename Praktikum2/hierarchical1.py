# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print(f"{self.nama} suara.")

class Serigala(Hewan):
    def __init__(self, nama):
        super().__init__(nama)

    def suara(self):
        print(f"{self.nama} Auuuuu!!")

class Kucing(Hewan):
    def __init__(self, nama):
        super().__init__(nama)

    def suara(self):
        print(f"{self.nama} meong!!")

HSerigala = Serigala("bold")
HKucing = Kucing("mely")

HSerigala.suara()
HKucing.suara()