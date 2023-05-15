import math

try:
    # Menghitung nilai faktorial dari suatu bilangan
    x = 10
    factorial = math.factorial(x)
    print("Nilai faktorial dari", x, "adalah", factorial)
    
    # Mencoba menghitung nilai faktorial yang terlalu besar
    y = 10000
    factorial = math.factorial(y)
    print("Nilai faktorial dari", y, "adalah", factorial)
    
except OverflowError as e:
    print("Terjadi kesalahan:", e)