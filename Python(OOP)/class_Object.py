class Students:
    Roll = ""
    Gpa = ""
    
shihab= Students()
# print(isinstance(shihab,Students))#is object created ? true
shihab.Roll=1
shihab.Gpa= 5
Sabbir= Students()
Sabbir.Roll = 2
Sabbir.Gpa = 4.75
shimul= Students()
shimul.Roll = 4
shimul.Gpa = 4.5
print(shihab.Gpa)

class Car:
    def __init__(self):
        self.model=""
        self.brand = ""
        
car1 = Car()
car1.brand="corrola"
car1.model="toyota"
print(car1.model,car1.brand)