class Car:
   def __init__(self):
        self.name= "sujuki" 
   
class Driver:
    def drive(self,car_name):
        print("driving",car_name.name)
        
c1= Car()
d1=Driver()
d1.drive(car_name=c1)

class Teacher:
    def __init__(self, name):
        self.t_name = name

class School:
    def __init__(self, name):
        self.s_name = name
        self.teachers = []

    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        self.f=self.teachers
        

t1 = Teacher("Mr. Smith")
s1 = School("Greenwood High")
s1.add_teacher(t1)
print(s1.name,"\n",s1.f[0].t_name)
