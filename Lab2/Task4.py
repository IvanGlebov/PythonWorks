#import math
#print(math.factorial(int(input())))
n = int(input("Enter n : "))
res = 1
for i in range(n+1):
    if i != 0:
        res *=i
print(res)
