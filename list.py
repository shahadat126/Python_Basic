# fruits =["apple","orange","banana","mango"]
# print(fruits)
# fruits.append("sour")
# fruits.pop
li =[1,2,3,4,5]
print(li)
li2=[6,7,8,9,10]
li.extend(li2)
print(li)
li2.extend(li)
print(li2)
#extend concat two list
#list1.extend(list2) after this operation its value assigned in list1
#list.insert(index,element)
li3=["a","b","c","d","b"]
li3.insert(0,"e")
print(li3)
#list.remove(element)
li3.remove("b")
print(li3)
#list.index(element)
print(li3.index("a"))
#list.pop(index)
x=li3.pop(0)
print(x)
print(li3)
#list.sort()
li3.sort()
print(li3)
#list.reverse()
li3.reverse()
print(li3)
x= "12345678"
y=list(x)
print(y)
print(y.index('3'))
y.reverse()
print(y)