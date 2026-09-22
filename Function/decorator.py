# def changecase(func):
#     return func().upper()
# @changecase    
# def main_func():
#     return "hello world"
    
# print(main_func)

# def changecase2(func): #main_func = changecase2(main_func)
#     def wrapper():
#         return func().upper()
#     return wrapper# main_func = wrapper
# @changecase2
# def main_func():
#     return "hello world" 
# print(main_func())# wrapper()

def changecase3(a):
    def wrapper(x):
        return a(x).upper()
    return wrapper

@changecase3
def main_func3(name):
    return "hello " + name 

print(main_func3("shahadat"))


def changecase4(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase4(4)
def myfunction():
  return "Hello Linus"

print(myfunction())