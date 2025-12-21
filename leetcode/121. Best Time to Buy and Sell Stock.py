class Solution:
    # O(N)
    def max_prices_at_slices(self, prices: List[int]) -> List[int]:
        """i:-1 -> max"""
        max_prices = [0] * len(prices)
        max_price = 0
        for i in range(len(prices) - 1, -1, -1):
            if max_price < prices[i]:
                max_price = prices[i]

            max_prices[i] = max_price
        
        return max_prices


    # O(N)
    def maxProfit(self, prices: List[int]) -> int:
        max_prices = self.max_prices_at_slices(prices)
        max_profit = 0
        for i in range(len(prices)):
            buy_price = prices[i]
            if max_prices[i] - buy_price > max_profit:
                max_profit = max_prices[i] - buy_price
        
        return max_profit
        