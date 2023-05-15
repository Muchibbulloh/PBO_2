def fibonacci():
    a, b = 0, 1
    while True:
        try:
            yield a
            a, b = b, a + b
        except GeneratorExit:
            print("Terjadi kesa;ahan maka akan ditutup.")
            return
            
f = fibonacci()

for i in f:
    print(i)
    if i > 100:
        f.close()