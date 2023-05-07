import math

class Bola:
    def __init__(self, r):
        self.r = r

    def volume(self):
        return 4/3 * math.pi * self.r ** 3

    def luas(self):
        return 4 * math.pi * self.r ** 2

def create_bola_class(name, radius_attr):
    def volume(self):
        return 4/3 * math.pi * getattr(self, radius_attr) ** 3

    def luas(self):
        return 4 * math.pi * getattr(self, radius_attr) ** 2

    return type(name, (object,), {
        'volume': volume,
        'luas': luas,
        '__init__': lambda self, r: setattr(self, radius_attr, r)
    })

DynamicBola = create_bola_class('DynamicBola', 'r')
b = DynamicBola(5)
print("Volume bola adalah:", b.volume())
print("Luas bola adalah:", b.luas())