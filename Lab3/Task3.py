a = [[], []] # Многомерный список (массив)
for i in range(1, 34):
    for j in range(1, i):
        print(chr(ord('А') + j - 1), end=' ')
    print()
