# 斐波那契数列
import numpy

def fib_matrix(n):
    res = pow((numpy.matrix([[1, 1], [1, 0]])), n) * numpy.matrix([[1], [0]])
    return res[0][0]

print(fib_matrix(3))

# 递归
# def fib(number):
#     fib[0], fib[1] = 0, 1
#     for i in range(2, number):
#         fib[i] = fib[i - 1] + fib[i - 2]
#     return fib[number]
    
# # 递推
# def fib(n):
#     f1 = f2 = 1
#     for k in range(n + 1):
#         f1, f2 = f2, f2 + f1
#     return f2

# 通项公式
# def power(a, n):
#     # 边界条件
#     if n < 0:
#         return 1 / power(a, -n)

#     if n == 0:
#         return 1

#     # r = power(a, n / 2)
#     # return r * r * a if n % 2 else r * r

#     res, tmp = 1, a
#     while n:
#         if n & 1:
#             res *= tmp
#         n >>= 1
#         tmp *= tmp
#     return res

# if __name__ == '__main__':
#     print(power(1, 6))