#stack last in first out
list1 = ["bangla"]
list1.append("english")
print(list1)
list1.append("math")
list1.append("SCIENCE")

list1.pop()
print(list1)
#queue fisrt in first out
from collections import deque
list2 = deque(["1","2","3","4"])
list2.popleft()
list2.popleft()
list2.popleft()
list2.popleft()

print(list2)
if not list2:
    print("No person left")