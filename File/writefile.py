with open('File/name.txt','w') as f:#w creates the files if does not exist and override the previous content
     f.write("hello world")
     
with open('File/name.txt','a') as f:# a creates the files if does not exist and add new content after the previous content
    f.write("\nhi")

lines = ['\n i love python\n','i am new to python\n']
with open('File/name.txt','a') as f:
    f.writelines(lines)

    