
def addition(a,b):
    result = a+b
    return result
r = addition(15,20)
print(r)

#type 2
def addition_multiple_arguments(*args):
    return sum(args)

result= addition_multiple_arguments(10,20,50,30,25,25,30)
print(result)