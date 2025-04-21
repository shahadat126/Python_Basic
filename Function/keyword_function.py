

# def my_function(l_name,age,f_name):
#     print(f"My name is  {f_name} {l_name}.I am {age} years old")
    
# my_function(f_name="Shimul",l_name="khan",age=28)
def my_function(**data):
    print(data)
    print(f"My name is  {data['f_name']} {data['l_name']}.I am {data['age']} years old. I Got {data['marks']} marks in programming. I live in {data['address']}")
    
my_function(f_name="Shimul",l_name="khan",age=28,marks = 95, address="Dhaka")