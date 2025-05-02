# import os
# if os.path.exists('name.txt'):
#     print("File exists")
# else:
#     print("File not found")
import pathlib
import os
file_path = pathlib.Path('File/name.txt')

if file_path.exists():
    print("File exists")
print(os.path.abspath('File/name.txt'))
print(os.path.getsize('File/name.txt'))
with open('File/name.txt','r') as f:
    print(f.read(18))
    print(f.tell())