

class Students :
   
    def __init__(self,roll,gpa):
        self.gender= "male".capitalize()
        self.city = "dhaka".capitalize()
        self.Roll= roll
        self.Gpa= gpa
        print(self) #it print  instance from __str__ method what i choose
    def __str__(self):
        return "Roll : {} | Gpa : {} | Gender: {} | City: {}".format(self.Roll,self.Gpa,self.gender,self.city) #return this instance into print(self) so that it print this return data without object calling

rahim= Students(101,4.5)
# print(rahim) it will neew when i did not use print(self) into the class

# class Car:
#     def __init__(self, model):
#         self.model1 = model  # self refers to car1

# car1 = Car("Toyota")
# print(car1.model1)  # Output: Toyota

