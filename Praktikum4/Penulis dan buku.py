class Penulis:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = []
    
    def tambah_buku(self, judul):
        self.buku.append(Buku(judul))
        
    def info(self):
        print(f"Nama Penulis: {self.nama}")
        print(f"Alamat: {self.alamat}")
        print("Buku yang ditulis:")
        for buku in self.buku:
            print("- " + buku.judul)
        print()
        

class Buku:
    def __init__(self, judul):
        self.judul = judul
    
    def info(self):
        print(f"Judul Buku: {self.judul}")



penulis1 = Penulis("Raditya dika", "Indonesia")
penulis2 = Penulis("Panji Pragiwaksono", "Indonesia")
penulis3 = Penulis("Ernest", "Indonesia")


penulis1.tambah_buku("Kambing jantan")
penulis1.tambah_buku("Manusia setengah salmon")
penulis1.tambah_buku("Ubur ubur lembur")
penulis2.tambah_buku("Menemukan indonesia")
penulis2.tambah_buku("Nasional its me")
penulis3.tambah_buku("Cek toko sebelah")


penulis1.info()
penulis2.info()
penulis3.info()