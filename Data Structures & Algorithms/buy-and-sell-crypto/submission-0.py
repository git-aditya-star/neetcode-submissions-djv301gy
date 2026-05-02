class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 0:
            return 0
        profit = 0
        buy = prices[0]
        sell = prices[0]
        for i in range(1, size):
            curr_val = prices[i]

            if curr_val < buy:
                buy = curr_val
                sell = curr_val
            elif curr_val > sell:
                sell = curr_val
                pro = sell-buy
                profit = max(pro, profit)
        return profit