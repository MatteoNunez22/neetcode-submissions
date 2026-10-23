class Solution:
    def trap(self, height: List[int]) -> int:
        # Find leftMaxes and rightMaxes
        n = len(height)
        l, r = 0, n - 1
        leftMax, rightMax = [0] * n, [0] * n
        lMax, rMax = 0, 0
        while l < n and r >= 0:
            lMax, rMax = max(lMax, height[l]), max(rMax, height[r])
            leftMax[l], rightMax[r] = lMax, rMax
            l += 1
            r -= 1
        
        water = 0
        for i in range(n):
            h = height[i]
            lM = leftMax[i]
            rM = rightMax[i]
            water += max(min(lM, rM) - h, 0)

        return water
