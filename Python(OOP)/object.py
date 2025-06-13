# x=["6"]
# print(type(x))

# def f():
#     pass
    
# print(type(f))
class Car:
    make='toyota'
    def __init__(self,mk,mdl,yr):
        self.make= mk
        self.model=mdl
        self.year=yr
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
        
    def move(self):
        print("the car is moving")
    
    def horn(self):
        print("beef beef!")
        
        
x=Car("l","k","y")
print(x)
print(type(x))
# mycar= Car()
# print(mycar.make)
# mycar.move()

mycar= Car('Subaru','Forestar' ,2014)
mycar.horn()
another_car = Car('Toyota','Camry', 2020)
another_car.move()
print(mycar.make,another_car.make)
print(mycar)
