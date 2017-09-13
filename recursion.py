def fact(x, y = 1):
    if x == 1:
        return 1 * y
    else:
        res = x * y
        return fact(x-1, res)
result = fact(6)
print(result)

total = sum([2, 4, 6])
print(total)
