# 求最大子数组之和问题：给定一个整数数组（数组元素有负有正），求其连续子数组之和的最大值。
# 状态转移方程： sum[i] = max(sum[i-1] + a[i], a[i])
def main():
    s = [12, -4, 32, -36, 12, 6, -6]
    print("定义的数组为：", s)
    s_max, s_sum = 0, 0
    for i in range(len(s)):
        s_sum += s[i]
        if s_sum >= s_max:
            s_max = s_sum # 不断更新迭代s_max的值，尽可能的令其最大
        elif s_sum < 0:
            s_sum = 0
    print("最大子数组和为：", s_max)
if __name__ == "__main__":
    main()