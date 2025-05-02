with open("File/name.txt","r") as fp:
   # content=fp.read()
    content=fp.readlines()#read all lines at once and process them as a list including \n
    print(content)