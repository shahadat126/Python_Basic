import math
class Fraction :
    def __init__(self,n,d):
        self.numerator = n
        self.denominator = d
        
    def add(self,f):
        l= math.lcm(self.denominator,f.denominator)
        num=(l/self.denominator)*self.numerator + (l/f.denominator)*f.numerator
        self.numerator=int(num)
        self.denominator=l
        
    def __str__(self):
        return "{} / {}".format(self.numerator,self.denominator)
f1=Fraction(5,10)
f2=Fraction(2,5)
f1.add(f2)
print(f1)


