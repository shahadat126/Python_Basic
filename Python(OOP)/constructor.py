class Student :
    
    def __init__(self,a,b):# constructor function/method
        self.roll= a
        self.gpa= b
        self.area= self.roll * self.gpa
    def __str__(self):
        return "Area : {}".format(self.area)
        
        
        
    
    
result1= Student(10,20)
result2= Student(100,200)

print(result1)
print(result2)
