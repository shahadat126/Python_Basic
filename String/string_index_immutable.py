a = "this is string"
print(a[0])
print(a[13])
# print(a[16])
#toatal index = total len - 1
print(len(a))
print(a[len(a)-1]) #last character print long method
print(a[-1]) #last character print short method 
print(a[-2]) #last 2nd character print short method

#immutable data type

b= "sabbir"
print(b[-2])
print(b[-5])
b[1] = 'o' #TypeError: 'str' object does not support item assignment
print(b)