

class Students :
   
    def __init__(self,roll,gpa):
        self.gender= "male"
        self.city = "dhaka"
        self.Roll= roll
        self.Gpa= gpa
        print("hi",self)
    def __str__(self):
        return "Roll : {} \n Gpa : {}".format(self.Roll,self.Gpa)

rahim= Students(101,4.5)
print(rahim.Roll)

class Car:
    def __init__(self, model):
        self.model1 = model  # self refers to car1

car1 = Car("Toyota")
print(car1.model1)  # Output: Toyota

