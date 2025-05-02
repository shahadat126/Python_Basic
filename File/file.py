


# how to read
# file= open("myfile","r")
# content = file.read()
# file.close()

with open('File/myfile.txt','r') as f:
    content = f.read()
    print(content)