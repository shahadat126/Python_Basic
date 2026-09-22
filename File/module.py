import csv


with open('contact.csv', "r",newline="") as f:
    reader = csv.reader(f)
    contact = list[reader]
    print(contact)
    for row in reader:
        print(row)


