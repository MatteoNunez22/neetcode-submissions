class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxPt = 0
        lowPr = prices[0]

        for price in prices:
            maxPt = max(price - lowPr, maxPt)
            lowPr = min(price, lowPr)
        
        return maxPt