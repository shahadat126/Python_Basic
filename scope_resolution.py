# x = 10
# def add():
#     y= 5
#     x=6
#     print(y)
#     print(x)
# add()
# print(x)

#LEGB
#Local 
# Enclosing 
# Global 
# Build in scope //(print,sum,max,input)

# n = 100  #global function
def outer():
    n="enclosing" #enclosing variable
    
    def inner():
         #this keyword only can change global variable
        print("a",n) #local variable
        
    inner()
    print("1",n)

outer()

# n = 100  #global function
# def outer():
    
#     n="enclosing" #enclosing variable
    
#     def inner():
#         nonlocal n #this keyword only can change enclosing variable
#         n="local" #local variable
        
#     inner()
#     print("1",n)

# outer()
# print(n)
    