class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            buy=min(prices[i],buy)
            profit = prices[i]-buy
            if profit> max_profit:
                max_profit = profit
        return max_profit

        