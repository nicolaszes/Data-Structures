# 斐波那契数列
def fib(number):
    fib[0], fib[1] = 0, 1
    for i in range(2, number):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[number]
    
if __name__ == '__main__':
    print(fib(35)) 