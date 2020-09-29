name = input()
a = name.find(' ')
print(name[:a] + ' ' + name[a+1] + '.' + name[name.find(' ', a+1) + 1])



