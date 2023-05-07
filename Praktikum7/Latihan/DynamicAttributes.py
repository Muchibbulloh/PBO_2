class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
person = person("jhon", 30)
    
# menambahkan atribut address secara dinamis
person.address = "123 Main St."
    
# mengubah nilain atribut age secara dinamis
person.age = 35
    
print(person.name)
print(person.age)
print(person.address)
