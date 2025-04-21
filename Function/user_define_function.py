#type1
#No input, no return

def my_first_function():#function definition
    a = 10
    b = 10
    print(a+b)
my_first_function()# function call

#type 2
#input , no return

def add_two_numbers(a,b): # arguments
    print(a+b)
add_two_numbers(10,20) #parameter
add_two_numbers(100,200)

#input,return
def multiply_two_numbers(a,b):
    return a*b
result = multiply_two_numbers(10,20)
print(result)

#no input, return
def hello():
    return "Hello"
get = hello()
print(get)
    