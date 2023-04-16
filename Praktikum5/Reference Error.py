try:
 # Mencoba mengakses variabel yang belum didefinisikan
    print(x)
except ReferenceError as e:
    print("Terjadi kesalahan:", e)