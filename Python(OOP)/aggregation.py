class Car:
    def __init__(self,car):
        self.car = car
        
        
class Engine:
    def start(self):
        print("Start Engine")

e1 =Engine()
c1 = Car(car=e1)
c1.car.start()





