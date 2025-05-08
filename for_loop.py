# fruits = ["apple","banana","orange","mango"]
# for i in range(4):
#     print(i+1,fruits[i])

# for i in range(1,11,2):
#     print(i)

# def multiplication(n):
#     print(n,"x",1,"=",n*1)
#     print(n,"x",2,"=",n*2)
#     print(n,"x",3,"=",n*3)
    
# multiplication(3)

# def multiplication(n):
#     print("{} x {} = {}".format(n,1,n*1))
#     print("{} x {} = {}".format(n,2,n*2))
#     print("{} x {} = {}".format(n,3,n*3))
#     print("{} x {} = {}".format(n,4,n*4))
    
    
# multiplication(3)
def multiplication(n):
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
   
    
    
multiplication(3)
