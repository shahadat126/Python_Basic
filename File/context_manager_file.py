with open("File/contact.csv", "r") as fp:
    content = fp.readline()  # read all lines at once and process them as a list including \n
    print(content)
