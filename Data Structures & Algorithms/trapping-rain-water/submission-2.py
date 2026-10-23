class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n == 0:
            return 0

        l, r = 0, n - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                res += max(maxL - height[l], 0)
                maxL = max(maxL, height[l])
            else:
                r -= 1
                res += max(maxR - height[r], 0)
                maxR = max(maxR, height[r])
        return res
