string = input()
count = 0
for i in range(len(string)):
    if string[i].isdigit():
      count += int(string[i])
print(count)
