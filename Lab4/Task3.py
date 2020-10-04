def add(instr):
    a = instr[:instr.find('+')]
    b = instr[instr.find('+') + 1: len(instr)]
    a = float(a)
    b = float(b)
    return a+b


def sub(instr):
    a = instr[:instr.find('-')]
    b = instr[instr.find('-') + 1: len(instr)]
    a = float(a)
    b = float(b)
    return a-b


def mul(instr):
    a = instr[:instr.find('*')]
    b = instr[instr.find('*') + 1: len(instr)]
    a = float(a)
    b = float(b)
    return a*b


def div(instr):
    a = instr[:instr.find(':')]
    b = instr[instr.find(':') + 1: len(instr)]
    a = float(a)
    b = float(b)
    if b == 0:
        return 'ERROE - can not divide on zero'
    else:
        return a/b


while True:
    string = input('enter expression to calculate')
    if string.find('+') > 0 :
        print(add(string))
    elif string.find('-') > 0:
        print(sub(string))
    elif string.find('*') > 0:
        print(mul(string))
    elif string.find(':') > 0:
        print(div(string))
    elif string.find('q') >= 0:
        break;
    else:
        print('Wrong expression! Try again')

