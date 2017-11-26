def fact(x, y = 1):
    if x == 1:
        return 1 * y
    else:
        res = x * y
        return fact(x-1, res)
print(fact(6))
print(sum([2, 4, 6]))
