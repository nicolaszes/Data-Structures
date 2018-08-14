def fact(x, y = 1):
    if x == 1:
        return 1 * y
    else:
        res = x * y
        return fact(x-1, res)
print(fact(6))
print(sum([2, 4, 6]))

def fib(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
if __name__ == '__main__':
    print fib(35)
