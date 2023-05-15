import sys

try:
    # Meminta input dari pengguna
    name = input("Masukkan nama Anda: ")
    
    if name == "":
        # Jika pengguna tidak memasukkan nama, program akan berhenti
        raise SystemExit("Program berhenti: nama tidak diberikan")

    else:
        # Jika pengguna memasukkan nama, program akan mencetak pesan selamat datang
        print("Selamat datang, " + name + "!")
        
except SystemExit as e:
    # Jika terjadi SystemExit, program akan mengeksekusi blok ini dan mencetak pesan error
    print("Terjadi kesalahan:", e)
    sys.exit(1)