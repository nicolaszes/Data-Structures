def main():
    d = [1, 2, 5, 10, 20, 50, 100] # 存储每种硬币面值
    d_num = [] # 存储每种硬币的数量
    total = 0
    # 拥有的零钱总和
    temp = input('请输入每种零钱的数量：')
    coinNum = temp.split(" ")

    for i in range(0, len(coinNum)):
        d_num.append(int(coinNum[i]))
        total += d[i] * d_num[i] # 计算出收银员拥有多少钱
    print(d_num)
    print(total)

    sum = float(input("请输入需要找的零钱:"))

    if sum > total:
        # 当输入的总金额比收银员的总金额多时，无法进行找零
        print("数据有错")
        return 0

    # total = total - sum
    # 要想用的钱币数量最少，那么需要利用所有面值大的钱币，因此从数组的面值大的元素开始遍历
    i = len(coinNum) - 1
    while i >= 0:
        if sum >= d[i]:
            n = round(int(sum / d[i]))
            if n >= d_num[i]:
                n = d_num[i]  # 更新n
            sum -= round(n * d[i]) # 贪心的关键步骤，令sum动态的改变，
            print("用了%d个%d元硬币"%(n, d[i]))
        i -= 1

if __name__ == "__main__":
    main()