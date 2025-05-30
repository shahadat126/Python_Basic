

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

a = [1,10,23,24,26,90]

result = []
# for i in a:
#     if i % 2 == 0:
#         result.append(i)
# print(result)

#list comprehension
new_result = [i for i in a if i %2==0]
print(new_result)

b=[1,2,3,4,5]
new_b = [i**2 if i % 2==0 else i for i in b]
print(new_b)