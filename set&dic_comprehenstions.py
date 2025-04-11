li =[(1,'one'),(2,'two'),(3,'three')]
dic={k:v for k , v in li}
print(dic)
dic={v:k for k,v in li}
print(dic)

s ='abbacaackdddkeffacbesde'
unique_letters= { c for c in s}
print(unique_letters)


colors_choice = [('irfan','blue'),('shakib','green'),('hafeej','light'),('shodi','black'),('amla','deep_G')]
colors_dic={name:color for name,color in colors_choice}
print(colors_dic)
colors_set={color for color in colors_dic.values()}
colors_name={name for name in colors_dic.keys()}
print(colors_name)
print(colors_set)