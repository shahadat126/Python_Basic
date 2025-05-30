# li = [1,2,3,4]
# tpl =(1,2,3,4)
# print(tpl,type(tpl))
# print(tpl[2],tpl[-1])
# print(li,type(li))
# li[0]=4
# print(li,type(li))
# tpl[0]=5
# print(tpl,type(tpl))
tpl=(1,2,3,4)
for item in tpl:
    print(item)

tpl1=1,2,3
a,b,c=tpl1
print(a,b,c)
 
t =(1,2,3)
print(t)
t = tuple(reversed(t))
print(t)