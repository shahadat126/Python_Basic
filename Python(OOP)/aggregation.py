# class Book:
#     def __init__(self, title,author):
#         self.title = title
#         self.author = author

# class Library:
#     def __init__(self):
#         self.books = []

#     def add_book(self, book):
#         self.books.append(book)

#     def show_books(self):
#         for book in self.books:
#             print(book.title,book.author)

# # Test
# b1 = Book("Python Basics","sk")
# b2 = Book("OOP in Python","khan")

# lib = Library()
# lib.add_book(b1)
# lib.add_book(b2)
# lib.show_books()

class Course:
    def __init__(self,title):
        self.title= title
class Student:
    def __init__(self,name):
        self.name = name
        self.course = []
    def enroll(self,course):
        self.course.append(course)
    def enroll_shows(self):
        for course in self.course:
            print(f"{self.name}  enrolled  in {course.title}")
        
c1 = Course("C")
c2 = Course("C++")
c3 = Course("python")

stu= Student("shahadat")
stu.enroll(c1)
stu.enroll(c2)
stu.enroll(c3)

stu.enroll_shows()