# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# class Employee(Person):
#     def __init__(self, name, age, emp_id, salary):
#         super().__init__(name, age)
#         self.emp_id = emp_id
#         self.salary = salary

#     def display_info(self):
#         super().display_info()
#         print(f"Employee ID: {self.emp_id}, Salary: {self.salary}")

# class Programmer:
#     def __init__(self, language):
#         self.language = language

#     def show_language(self):
#         print(f"Programming Language: {self.language}")

# class Developer(Employee, Programmer):
#     def __init__(self, name, age, emp_id, salary, language):
#         Employee.__init__(self, name, age, emp_id, salary)
#         Programmer.__init__(self, language)

#     def show_details(self):
#         self.display_info()
#         self.show_language()

# # Testing
# dev = Developer("Rafi", 25, "EMP123", 50000, "Python")
# dev.show_details()
# print(Developer.mro())
