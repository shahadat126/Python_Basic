# i = 1
# while i <= 10:
#   print("Hello world")
#   i=i+1

def multiplication(n):
    for i in range(1,11):
        print("{} x {} = {}".format(n,i,n*i))
   
    
n= input("enter a number")
n=int(n)
while n!=0:
  multiplication(n)
  print(" ")
  n=input("enter a number")
  n=int(n)
  