class Animal:
    def speak(self):
        print("Animal speaks")

class Cat(Animal):  # Single inheritance
    def bark(self):
        print("Cat barks")

d = Cat()
d.speak()  # parent class method
d.bark()   # child class method

class Animal:
    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):
    def __init__(self):
        print("Dog Constructor")

d = Dog()

#যেহেতু Dog ক্লাস নিজের __init__() তৈরি করেছে, তাই এটি override করেছে।
#Parent এর constructor আর কল হবে না, কারণ Python শুধু Dog.__init__() দেখছে।

#type 2
#if আমরা চাই Parent এর constructor ও কল হোক?
#তাহলে আমরা super() ব্যবহার করি।
class Animal2:
    def __init__(self):
        print("Animal Constructor")

class Dog2(Animal2):
    def __init__(self):
        super().__init__()  # Parent class constructor call
        print("Dog2 Constructor")

d = Dog2()

# | Dog ক্লাসে `super()` না থাকলে | থাকলে                                              |
# | ----------------------------- | -------------------------------------------------- |
# | শুধু child constructor চলে    | প্রথমে parent constructor, তারপর child constructor |
