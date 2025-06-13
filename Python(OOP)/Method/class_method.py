# class Car:
#     @classmethod
#     def drive(cls):
#         print("He is driving a Car")
        
# Car.drive()
# class Student:
#     total_students = 0
#     def __init__(self,name):
#         self.name= name
#         Student.total_students +=1
        
#     @classmethod
#     def get_total_students(cls):
#         return cls.total_students
    
# s1= Student("shimul")
# s1= Student("shimul1")
# s1= Student("shimul2")
# print(s1.get_total_students())

# print(Student.total_students)
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_dict(cls, data):
        name, price = data.split(',')
        return cls(name,price)

p = Product.from_dict("keya,20")
print(p.name) # Output: Shampoo
print(p.price)  # Output: 120
# একটি Book ক্লাস বানাও, যাতে from_string নামে একটি classmethod থাকে। ইনপুট হবে: "Harry Potter, J.K. Rowling"
# তুমি split করে title ও author বের করবে এবং সেই অনুযায়ী object তৈরি করবে
class Book:
    def __init__(self,title,author):
        self.title= title
        self.author= author
    @classmethod
    def from_string(cls,data):
        title, author = data.split(',')
        return cls(title,author)
    
b = Book.from_string("Harry Potter, J.K. Rowling")
print(b.title)