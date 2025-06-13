class Product:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_dict(cls, data):     # ← 🔸 This is the factory method
        name, age = data.split(',')
        return cls(name, int(age))  # ← Creates and returns a Product object

p = Product.from_dict("keya,28")  # ← 🔸 Using the factory method
print(p.name)
print(p.age)