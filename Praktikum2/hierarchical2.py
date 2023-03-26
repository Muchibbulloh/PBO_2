# NAMA  : MUHAMAD MUCHIBBULLOH
# KELAS : R2 (B)
# NIM   : 210511078

class Teknik:
	def jurusan(self):
		print("Di umc memiliki jurusan teknik.")
class Peternakan(Teknik):
	def faultas1(self):
		print("Fakultas teknik peternakan.")
class Informatika(Teknik):
	def fakultas2(self):
		print("Fakultas teknik Informatika.")

object1 = Peternakan()
object2 = Informatika()
object1.jurusan()
object1.faultas1()
object2.jurusan()
object2.fakultas2()