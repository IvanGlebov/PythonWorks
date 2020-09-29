n, m = int(input()), int(input())
for i in range(1, n+1):
    for j in range(1, m+1):
        print(j**i, end=' ')
    print()
