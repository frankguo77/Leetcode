class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        max_profit = 0
        mini_p = prices[0]
        for i in range(1, n):
            if prices[i] > mini_p:
                max_profit = max(max_profit, prices[i] - mini_p)
            else:
                mini_p = prices[i]
        return max_profit