class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    @classmethod
    def default_car(cls):
        print("sk")  # This will print when using the default constructor
        return cls(name="sk", brand="")

    @classmethod
    def named_car(cls, name, brand):
        return cls(name=name, brand=brand)

# Parameterized constructor
car1 = Car.named_car("apache", "sujuki")
print(car1.name, car1.brand)

# Default constructor
car2 = Car.default_car()
print(car2.name, car2.brand)

# Another default
car3 = Car.default_car()
print(car3.name)
