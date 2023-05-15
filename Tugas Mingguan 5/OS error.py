import os

try:
    # Membuat sebuah direktori baru
    os.mkdir("testdir")
    print("Direktori berhasil dibuat!")
    
    # Mengubah nama direktori
    os.rename("testdir", "newdir")
    print("Direktori berhasil diubah namanya!")
    
    # Menghapus direktori
    os.rmdir("newdir")
    print("Direktori berhasil dihapus!")
    
    # Mencoba mengakses direktori yang sudah dihapus
    os.listdir("newdir")
    
except OSError as e:
    print(" Terjadi kesalahan pada", e)