class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max_profit = 0
        max_cost = None
        for b in range(days):
            
            if max_cost and max_cost[1] > b:
                if max_profit < max_cost[0] - prices[s]:
                    max_profit = max_cost[0] - prices[s]
                continue
            
            for s in range(b, days):
                if max_profit < prices[s] - prices[b]:
                    max_profit = prices[s] - prices[b]
                    min_profit = (prices[b], b)
                
        return max_profit
