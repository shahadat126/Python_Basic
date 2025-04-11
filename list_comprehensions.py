li = ['apple','banana','orange','mango']
fruits = [x.capitalize() for x in li]
print(fruits)
   
li_len= [len(x) for x in li]
print(li_len)

cube_list = [x*x*x for x in range(1,11)]
print(cube_list)

cube_list2 = [x*x*x for x in range(1,11) if x % 2==1]
print(cube_list2)
cube_list3 = [x for x in range(1,11) if x % 2==1]
print(cube_list3)