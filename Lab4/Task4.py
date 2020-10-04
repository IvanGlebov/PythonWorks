import math


def findlen(xy1, xy2):
    x1 = xy1[:xy1.find(',')]
    y1 = xy1[xy1.find(',') + 1:len(xy1)]
    x2 = xy2[:xy2.find(',')]
    y2 = xy2[xy2.find(',') + 1:len(xy2)]
    x1, x2, y1, y2 = float(x1), float(x2), float(y1), float(y2)
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


def findarea(a, b, c):
    return math.sqrt(((a+b+c)/2)*(((a+b+c)/2)-a)*(((a+b+c)/2)-b)*(((a+b+c)/2)-c))


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"


print("Enter pentagon tops in current way: ")
print("        x1,y1       ")
print("         / \        ")
print("        /   \       ")
print(" x5,y5 /     \ x2,y2")
print("       \     /      ")
print("  x4,y4 \___/  x3,y3")
print("Entered coordinates should be separated by ','")
print("Example : 1,3 ")
x1y1 = input('Enter x1,y1')
x2y2 = input('Enter x2,y2')
x3y3 = input('Enter x3,y3')
x4y4 = input('Enter x4,y4')
x5y5 = input('Enter x5,y5')
area = findarea(findlen(x1y1, x3y3),
                findlen(x3y3, x4y4),
                findlen(x4y4, x1y1)) + \
       findarea(findlen(x1y1, x4y4),
                findlen(x4y4, x5y5),
                findlen(x5y5, x1y1)) + \
       findarea(findlen(x1y1, x3y3),
                findlen(x3y3, x2y2),
                findlen(x2y2, x1y1))
print(toFixed(area, 3))
