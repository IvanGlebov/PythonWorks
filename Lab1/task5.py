import math
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
p = (a+b+c)/2
res = math.sqrt(((p-a)*(p-b)*(p-c)))
print(res)
