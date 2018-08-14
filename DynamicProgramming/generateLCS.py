def lcs_dp(self, input_x, input_y):
    # input_y as column, input_x as row
    dp = [([0] * (len(input_y)+1)) for i in range(len(input_x)+1)]
    for i in range(1, len(input_x)+1):
        for j in range(1, len(input_y)+1):
            if i == 0 or j == 0:  # 在边界上，自行+1
                    dp[i][j] = 1
            elif input_x[i-1] == input_y[j-1]:  # 不在边界上，相等就加一
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # 不相等
                dp[i][j] = max(dp[i - 1][j], dp[i][j -1])
    for dp_line in dp:
        print(dp_line)
    return dp[-1][-1]