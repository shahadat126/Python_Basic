with open("name.txt", "r") as fp:
    content = fp.reader()  # read all lines at once and process them as a list including \n
    print(content)
