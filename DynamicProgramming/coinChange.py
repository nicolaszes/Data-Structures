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
from collections import defaultdict
lookup = defaultdict(int)
    
class Solution:
    def coinChange(self, coins: 'List[int]', amount: 'int') -> 'int':
        if amount < 1:
            return 0

        def helper(amount):
            if amount < 0:
                return -1
            if amount == 0:
                return 0
            if lookup[amount]:
                return lookup[amount]

            min_num = 2 ** 31 - 1
            for coin in coins:
                res = helper(amount - coin)
                # min_num = min(min_num,res + 1)
                if res >= 0 and res < min_num:
                    min_num = res + 1
            lookup[amount] = min_num if min_num != 2 ** 31 - 1 else -1
            return lookup[amount]

        return helper(amount)