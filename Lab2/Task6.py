n = int(input("Enter right border : "))

for i in range(1, n):
    flag = 1
    for j in range (2, i-1):
        if i%j == 0:
            flag = 0
    if flag == 1:
        print(i)
