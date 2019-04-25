class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DFS O(2^N)
        print(111)
        # Greedy O(N)
        profit = 0
        for i, x in enumerate(prices):
            if i == len(prices) - 1: return profit
            # 如果后一天的价格比前一天高，就说明有利可图，可以实行低买高抛
            if x < prices[i+1]:
                profit += prices[i+1] - x
        return profit

        # DP O(N)