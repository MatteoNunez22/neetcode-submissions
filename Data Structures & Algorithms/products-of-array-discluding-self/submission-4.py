class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        leftP = [0] * n
        output = [0] * n

        product = 1
        for i in range(n):
            leftP[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(n - 1, -1, -1):
            output[i] = leftP[i] * product
            product *= nums[i]
        
        return output
