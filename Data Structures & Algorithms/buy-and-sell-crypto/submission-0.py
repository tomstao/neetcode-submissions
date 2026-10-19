class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return
        buy = prices[0]

        max_sell = 0

        for price in prices:
            buy = min(buy, price)

            if price - buy > 0:
                max_sell = max(max_sell, price - buy)
        return max_sell

        