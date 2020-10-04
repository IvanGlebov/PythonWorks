prev = cur = 1
number = input('enter number')
number = int(number)
for i in range(int(number - 2)):
    temp = cur + prev
    prev = cur
    cur = temp
print(cur)
