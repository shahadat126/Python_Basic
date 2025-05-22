class Car:
    @classmethod
    def drive(cls):
        print("He is driving a Car")
        
    def engine(self):
        print("Starting the engine")
    @staticmethod
    def engine1():
        print("Starting the autoengine") #static method did not use any variable or call any function
        
Car.drive()
c1= Car()
c1.engine()
c1.engine1()