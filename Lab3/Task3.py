a = [[], []] # Многомерный список (массив)
for i in range(0, 33):
    a.append([])
    for j in range(0, i-1):
        a[i].append(chr(ord('А') + j))


print(a)


