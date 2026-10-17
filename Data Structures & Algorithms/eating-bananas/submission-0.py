class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) # Bounds
        res = r
        while l <= r:
            k = (l + r) // 2

            # Get hours to eat piles
            hrs = 0
            for pile in piles:
                hrs += math.ceil(pile/k)

            # Exceeds target
            if hrs > h:
                l = k + 1
            # Acceptable rate
            else: 
                res = k # Current lowest rate
                r = k - 1

        return res