'''
1,递归法
'''
def fib_recur(n):
    assert n >0,'n应该>0'
    if n == 1 or n == 2:
        return 1
    return(fib_recur(n-1) + fib_recur(n-2))
 
# test 输出前15个数
for i in range(1,16):
    print(fib_recur(i))

'''
2.递推法
'''
def fib_loop(n):
    assert n > 0,'n应该>0'
    a, b = 0, 1
    for i in range(n):
        a,b = b, a + b  # a = b,b = a + b，相当于 temp=b, b=a+b, a=temp
    return a
 
# 输出前15个数
for i in range(1,16):
    print(fib_loop(i))