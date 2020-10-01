a = [[], []] # Многомерный список (массив)
for i in range(0, 33):
    a.append([])
    for j in range(0, i-1):
        a[i].append(chr(ord('А') + j))
        #print(chr(ord('А') + j - 1), end=' ')

print(a)
#for i in range(0, 33):
##    for j in range(0, 33):
 #       print(a[i][j], end=' ')
 #   print()

