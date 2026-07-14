class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        max_p=0
        sell=None
        for i in range(1,len(prices)):
            sell=prices[i]
            profit =sell-buy
            if prices[i]<buy:
                buy =  prices[i]
            max_p=max(profit,max_p)
        return max_p