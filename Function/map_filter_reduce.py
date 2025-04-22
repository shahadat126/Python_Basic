nums = [1,2,3,4]

result = list(map(lambda x: x*x,nums))
print(result)
#filter
nums = [1,2,3,4,5]
even = list(filter(lambda x: x>2,nums))
print(even)
#reduce
import functools
sum = functools.reduce(lambda x,y : x+y,nums)
print(sum)