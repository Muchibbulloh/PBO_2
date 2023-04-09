class Peneliti:
    def __init__(self, nama, judul, tahun):
        self.nama = nama
        self.judul = judul
        self.tahun = tahun
    def penelitian(self):
        print(f"{self.nama} sedang melakukan penelitian {self.judul} di tahun {self.tahun}")

class Jurnalis:
    def __init__(self, nama, judul, tahun):
        self.nama = nama
        self.judul = judul
        self.tahun = tahun
    def liputan(self):
        print(f"{self.nama} sedang melakukan liputan {self.judul} di tahun {self.tahun}")

def compose(*functions):
    def composed():
        for f in functions:
            f()
    return composed

peneliti1 = Peneliti("Tukiyem", "Obat tradisional", 2015)
jurnalis1 = Jurnalis("Bang dodo", "Arus mudik", 2018)
peneliti_jurnalis = compose(peneliti1.penelitian, jurnalis1.liputan)
peneliti_jurnalis()
