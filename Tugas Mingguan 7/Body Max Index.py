class BMI:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    def hitung(self):
        return self.berat / ((self.tinggi/100) ** 2)

def create_bmi_class(name, berat_attr, tinggi_attr):
    def hitung(self):
        return getattr(self, berat_attr) / ((getattr(self, tinggi_attr) / 100) ** 2)

    return type(name, (object,), {
        'hitung': hitung,
        '__init__': lambda self, berat, tinggi: setattr(self, berat_attr, berat) or setattr(self, tinggi_attr, tinggi)
    })

DynamicBMI = create_bmi_class('DynamicBMI', 'berat', 'tinggi')
bmi = DynamicBMI(58, 173)
print("===================================================================")
print("BMI anda adalah:", bmi.hitung())
print("")
print("kurang dari 18,5 nilai BMI anda kurang")
print("jika nilai BMi anda diantara 18,5 - 22,9 ideal")
print("dan jika nilai BMI anda lebih dari 22,9 nilai BMI anda berlebihan")
print("===================================================================")