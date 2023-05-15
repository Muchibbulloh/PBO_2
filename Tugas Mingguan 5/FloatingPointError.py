try:
    x = 1.0
    y = 0.0
    z = x / y
    print(z)
    
except FloatingPointError:
    print("Terjadi ketika terjadi kesalahan dalam operasi bilangan pecahan")