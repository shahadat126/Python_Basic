#task1

name = input("Enter seller's name = ")
fixed_salary = float(input("Enter fixed_salary = "))
total_sales = float(input("Enter total_sales = "))

total_salary = fixed_salary + (total_sales * 0.15)

print(f"TOTAL = R$ {total_salary:.2f}")


#task2

A = float(input())
B = float(input())
C = float(input())

median = (A * 2 + B * 3 + C * 5) / 10

print(f"MEDIAN = {median:.1f}")
