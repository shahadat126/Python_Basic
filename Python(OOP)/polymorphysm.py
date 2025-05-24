class Shape:
    def area(self,a,b=10):
        return a*b
    
c = Shape()
c.area(10)
print(c.area(12,12))