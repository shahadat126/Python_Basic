class Heart:
    def __init__(self):
        print("Heart is beating")
        
class Human:
    def __init__(self):
        print("creating a human")
        self.heart= Heart() #creat a object in inner class but object from outer class
        
h = Human()