for i in range(1000, 9999):
    flag = 1
    n1 = i // 1000
    n2 = (i // 100)%10
    n3 = (i%100) // 10
    n4 = i % 10
    if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
        flag = 0
    if flag == 1:
        print(i)

