class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if N < 2:
            return 0
        
        # buy = [-float('inf')] * N 
        # sell = [0] * N
        # for i in range(N):
        #     buy[i] = max((buy[i - 1] if i > 0 else -float('inf')), (sell[i - 2] if i > 1 else 0) - prices[i])
        #     sell[i] = max((sell[i - 1] if i > 0 else 0), (buy[i - 1] if i > 0 else -float('inf')) + prices[i])
        # return sell[-1]
        
        buy = float('-inf')
        sell = sell1 = sell2 = 0
        for i in range(N):
            buy = max(buy, sell2 - prices[i])
            sell = max(sell1, buy + prices[i])
            
            sell2, sell1 = sell1, sell
            # buy1 = buy
        return sell
        