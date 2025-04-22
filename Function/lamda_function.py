#type 1
# result= lambda x: x*x
# print(result(2))
#type 2
# result= (lambda x: x*x) (2)
# print(result)
students =  [('abir',94,50),('shimul',85,25),('jahir',95,20)]
students_results = sorted(students,key= lambda x : x[2])
print(students_results)
students_results = sorted(students,key= lambda x : x[1])
print(students_results)