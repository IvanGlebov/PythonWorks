a = []
counter = 0
while True:
    try:
        e = float(input())
        a.append(e)
        counter += e
    except:
        print(counter/len(a))
        break;
