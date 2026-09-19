class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        i, j = 0, 1
        while i < j and j < len(prices):
            if prices[j] <= prices[i]:
                i = j
                j = i + 1
            else:
                p = prices[j] - prices[i]
                maxP = max(p, maxP)
                j += 1

        return maxP