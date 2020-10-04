a = [[], []] # Многомерный список (массив)
for i in range(0, 34):
    a.append([])
    for j in range(0, i-1):
        print(chr(ord('А') + j), end=" ")
        a[i].append(chr(ord('А') + j))
    print("")




