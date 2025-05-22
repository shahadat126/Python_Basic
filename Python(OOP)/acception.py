class Car:
   def __init__(self):
        self.name= "sujuki" 
   
class Drive:
    def drive(self,car):
        print("driving",car.name)
        
c1= Car()
d1=Drive()
d1.drive(car=c1)
