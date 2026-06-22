class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        Left = 0
        Right = 1
        max_profit = 0

        while Right < len(prices):
            if prices[Right] > prices[Left]:
                new_profit = prices[Right] - prices[Left]
                max_profit = max(max_profit, new_profit)
            else:
                Left = Right
            Right += 1
        return max_profit




        
        