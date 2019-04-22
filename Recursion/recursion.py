# 递归模版
'''
def recursion(level, param1, parma2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        print_result
        return
    
    # process logic in current level
    process_data(level, data...)

    # drill down
    self.recursion(level + 1, p1, ...)

    # reverse the current level status if needed
    reverse_state(level)
'''


# 斐波那契数列
def fib(number):
    if number == 0 or number == 1:
        return 1
    else:
        return fib(number - 1) + fib(number - 2)
if __name__ == '__main__':
    print(fib(35)) 

# 阶乘函数
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n - 1)

def fact(x, y = 1):
    if x == 1:
        return 1 * y
    else:
        res = x * y
        return fact(x-1, res)
print(fact(6))
print(sum([2, 4, 6]))