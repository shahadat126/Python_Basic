


# how to read
# file= open("myfile","r")
# content = file.read()
# file.close()
f = open('name.txt')
print(f.read())
with open('myfile.txt','r') as f:#when we use with keyword then we dont need to use close() for with because it automatically close the file
    content = f.read()
    print(content)
    
