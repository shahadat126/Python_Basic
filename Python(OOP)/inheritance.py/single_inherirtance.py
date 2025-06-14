class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Single inheritance
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # parent class method
d.bark()   # child class method
