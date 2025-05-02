# with open('File/name.txt','w') as f:
#      f.write("hello world")
     
with open('File/name.txt','a') as f:
    f.write("\nhi")

lines = ['\n i love python\n','i am new to python\n']
with open('File/name.txt','a') as f:
    f.writelines(lines)

    