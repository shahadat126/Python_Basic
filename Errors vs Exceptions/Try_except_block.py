try:
    with open("./File/name.txt",'r') as f:
        print(f.read())
    print(10/0)
    x = int("12")
    print(x)
    a =[1,2,3]
    print(a[1]) 
       

except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("Error : Divided by zero is not possible")
except IndexError:
    print("invalid index")
except Exception as e:
    print("Unknown error",e)

# প্রশ্ন	

# উত্তর
# একটি try block-এ দুটি error থাকলে কী হয়?
# প্রথম error-এ execution থামে


# দ্বিতীয় error কি execute হবে?
# না, সাধারণত হবে না

# Matching except কী হবে?
# প্রথম exception-এর matching handler

# প্রথম error handle হলে program কি পুরো শেষ?
# না, বাইরের code চলতে পারে

# দুটি error আলাদাভাবে handle করা সম্ভব?
# হ্যাঁ, আলাদা try-except ব্যবহার করে

# প্রথম error handle না হলে?
# Unhandled exception হয়ে program থেমে যেতে পারে