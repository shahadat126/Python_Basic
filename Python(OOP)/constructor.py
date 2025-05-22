class Student :
    
    def __init__(self,a,b):# constructor function/method
        self.roll= a
        self.gpa= b
    def Area(self):
        area = self.roll  * self.gpa
        print(area)
        
        
    
    
result1= Student(10,20)
result2= Student(100,200)

result1.Area()
result2.Area()