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

mycar= Car("A","B","C")
print((mycar))
print(mycar.make)
mycar.move()

# mycar= Car('Subaru','Forestar' ,2014)
# mycar.horn()
# another_car = Car('Toyota','Camry', 2020)
# another_car.move()
# print(mycar.make,another_car.make)
# print(mycar)
# এদের কাজের ক্রম (Execution Order)
# আপনি যখন একটি অবজেক্ট তৈরি করেন (যেমন: obj = Student()), তখন পাইথন ব্যাকগ্রাউন্ডে নিচের দুটি ধাপ পরপর সম্পন্ন করে:
# text
# ১. Student.__new__() ──> মেমোরিতে অবজেক্ট তৈরি করে (Object Creation)
#          │
#          ▼
# ২. Student.__init__() ──> তৈরি হওয়া অবজেক্টে ডাটা সেট করে (Object Initialization)
