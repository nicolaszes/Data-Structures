# 设汽车加满油后可行驶n公里，且旅途中有k个加油站
def main(n, k, d):
    num = 0
    # 表示加油次数
    for i in range(k):
        if d[i] > n:
            print('no solution')
            # 如果距离中得到任何一个值大于 n，则无法计算

    i = 0
    s = 0
    while i <= k:
        s += d[i]
        if s >= n:
            # 当局部和大于 n时则局部和更新为当前距离
            s = d[i]
            print(d[i])
            # 贪心意在令每一次加满油之后跑尽可能多的距离
            num += 1
        i += 1
    print(num)

if __name__ == '__main__':
    n = 100
    k = 5
    d = [50, 80, 39, 60, 40, 32]
    main(n, k, d)