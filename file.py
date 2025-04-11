# fp = open('myfile.txt','r')
fp=open('myfile.txt','a')

# fp.write("this is test file\n")
lines=["Apple\n","Banana\n","Orange\n"]
fp.writelines(lines)
# content = fp.read()
fp.close()