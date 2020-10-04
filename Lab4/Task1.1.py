def fib(n):
    res = 1
    if n > 2:
        res = fib(n-1) + fib(n-2)
    return res


number = input('enter number')
number = int(number)
print(fib(number))
