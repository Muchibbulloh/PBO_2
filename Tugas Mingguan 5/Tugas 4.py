class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas
        self.nilai = Nilai()
        
    def info(self):
        print(f"Nama Siswa: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print("mata pelajaran")
        self.nilai.info()
        print()
        

class Nilai:
    def __init__(self):
        self.mtk = None
        self.bhs_indonesia = None
        self.bhs_inggris = None
    
    def info(self):
        if self.mtk is None and self.bhs_indonesia is None and self.bhs_inggris is None:
            print("Belum ada nilai yang dimasukkan.")
        else:
            if self.mtk is not None:
                print(f"Matematika: {self.mtk}")
            if self.bhs_indonesia is not None:
                print(f"Bahasa Indonesia: {self.bhs_indonesia}")
            if self.bhs_inggris is not None:
                print(f"Bahasa Inggris: {self.bhs_inggris}")
        print()

siswa1 = Siswa("Muchib", "XII IPS 2")
siswa2 = Siswa("Aulia", "XII  OTKP 2")


siswa1.nilai.mtk = 87
siswa1.nilai.bhs_indonesia = 95
siswa2.nilai.bhs_inggris = 95
siswa2.nilai.mtk = 88

siswa1.info()
siswa2.info()