try:
    with open("name.txt",'r') as f:
        print(f.read())
    print(10/1)
    x = int("12")
    print(x)
    a =[1,2,3]
    print(a[1]) 
    x = abc   

except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Error : Divided by zero is not possible")
except IndexError:
    print("invalid index")
except Exception as e:
    print("Unknown error",e)
else:
    print("code executed successfully")
finally:
    print("Good job")
    
def check_file(filename):
    if filename == "":
        raise FileNotFoundError("file not found")
        
    if not filename.endswith('.txt'):
        raise  ("only .txt files are allowed")
    print("file correct")
try:    
    check_file('data.csv')
except Exception as e:# e = ValueError("only .txt files are allowed") 
    print("exception 1",e)