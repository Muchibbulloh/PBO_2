class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def volume(self):
        return self.sisi ** 3

    def luas(self):
        return 6 * self.sisi ** 2

def create_kubus_class(name, sisi_attr):
    def volume(self):
        return getattr(self, sisi_attr) ** 3

    def luas(self):
        return 6 * getattr(self, sisi_attr) ** 2

    return type(name, (object,), {
        'volume': volume,
        'luas': luas,
        '__init__': lambda self, sisi: setattr(self, sisi_attr, sisi)
    })

DynamicKubus = create_kubus_class('DynamicKubus', 'sisi')
k = DynamicKubus(5)
print("Volume kubus adalah:", k.volume())
print("Luas kubus adalah:", k.luas())