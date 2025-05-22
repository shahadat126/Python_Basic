#compile time ,run time
# Errors ----> Compile time error
#         ---> SyntaxError,IndentationError
# Exception ---> RuntimeError
#           ---> Indexing, key, value , ZeroDivisionError
try:
    with open('sabbir.txt','r') as f:
     print(f.read())
except IndexError:
    print("File not found")