# try:
#     fp = open("mynewfile.txt","r")
#     content=fp.read()
#     fp.close()
# except FileNotFoundError:
#     print("Your file is not found")
# try:
#     n1=10
#     n2=0
#     print(n1/n2)
# except ZeroDivisionError:
#     print("division is not allwoed by zero")
while True:    
    n1=int(input("Enter a number: "))
    n2=int(input("Enter another number: "))
    if n1==0 and n2==0:
        break
    try:
        print("result of division\n", n1/n2)
    except ZeroDivisionError:
        print("can not divide by zero")
    else :
        print("good work")
        break
    