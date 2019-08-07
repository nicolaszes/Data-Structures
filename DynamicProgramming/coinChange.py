# DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float("inf") else -1


# DFS
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        self.res = float("inf")
        n = len(coins)
        if amount == 0:
            return 0
        coins.sort(reverse = True)
        if amount < coins[-1]:
            return -1

        def dfs(loc, remain, count):
            if remain == 0:
                self.res = min(self.res, count)
            else:
                for i in range(loc, n):
                    if coins[i] <= remain < coins[i] * (self.res - count):
                        dfs(i, remain - coins[i], count + 1)

        for i in range(n):
            dfs(i, amount, 0)
        return self.res if self.res != float("inf") else -1