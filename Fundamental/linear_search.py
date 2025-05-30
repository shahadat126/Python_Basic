li = [1,2,6,10,100,14,5,9]
# found = li.index(5)
# found = 5 in li
# print(found)


# key = 6 
# flag= False
# for item in li:
#     if key==61:
#         print("found")
#         flag=True
#         break
# if flag is False:
#     print("not found")   

key=141
found=False
for item in li:
    if key==item:
        found=True
    
if found is True:
    print("found")
else:
    print("not found")