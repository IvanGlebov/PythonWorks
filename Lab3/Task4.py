n, m = int(input()), int(input())
a = [[], []]
for i in range(1, n+1):
    a.append([])
    for j in range(1, m+1):
        a[i].append(i**j)
