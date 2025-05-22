class Car:
   def __init__(self):
        self.name= "sujuki" 
   
class Driver:
    def drive(self,car):
        print("driving",car.name)
        
c1= Car()
d1=Driver()
d1.drive(car=c1)
