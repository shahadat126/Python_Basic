# num_to_words = dict()
# num_to_words[1]= 'one'
# num_to_words[2]= 'two'
# num_to_words[3]= 'three'
# print(num_to_words,type(num_to_words))

num_to_words = {1: 'one', 2: 'two', 3: 'three'}
fruits={'S':'Shimul','K':'Keya'}
print(fruits.get('K'))
num_to_words[4]='four'
print(num_to_words)
print(num_to_words[3])
if 5 in num_to_words:
    print("Available")
else:
    print("Not Found ")
del num_to_words[3]
print(num_to_words.items())
print(num_to_words.values())
print(num_to_words.keys())
print(num_to_words.get(1))


for key, value in num_to_words.items():
    print(key, value)
    