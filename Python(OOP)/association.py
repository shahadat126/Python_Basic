class Car:
   def __init__(self):
        self.name= "sujuki" 
   
class Driver:
    def drive(self,car_name):
        print("driving",car_name.name)
        
c1= Car()
d1=Driver()
d1.drive(car_name=c1)