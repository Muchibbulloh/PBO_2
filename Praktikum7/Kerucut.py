import math

class Kerucut:
    def __init__(self, r, t):
        self.r = r
        self.t = t

    def volume(self):
        return math.pi * self.r ** 2 * self.t / 3

    def luas(self):
        s = math.sqrt(self.r ** 2 + self.t ** 2)
        return math.pi * self.r * s + math.pi * self.r ** 2

def create_kerucut_class(name, radius_attr, height_attr):
    def volume(self):
        return math.pi * getattr(self, radius_attr) ** 2 * getattr(self, height_attr) / 3

    def luas(self):
        s = math.sqrt(getattr(self, radius_attr) ** 2 + getattr(self, height_attr) ** 2)
        return math.pi * getattr(self, radius_attr) * s + math.pi * getattr(self, radius_attr) ** 2

    return type(name, (object,), {
        'volume': volume,
        'luas': luas,
        '__init__': lambda self, r, t: setattr(self, radius_attr, r) or setattr(self, height_attr, t)
    })

DynamicKerucut = create_kerucut_class('DynamicKerucut', 'r', 't')
k = DynamicKerucut(5, 10)
print("Volume kerucut adalah:", k.volume())
print("Luas kerucut adalah:", k.luas())