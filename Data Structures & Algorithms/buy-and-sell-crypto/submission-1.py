class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,1

        profit = 0

        for i in range(len(prices) - 1):
            if prices[i + 1] > prices[left]:
                profit = max(profit, prices[i + 1] - prices[left])
                right = i + 1
            else:
                left = i + 1
        return profit


