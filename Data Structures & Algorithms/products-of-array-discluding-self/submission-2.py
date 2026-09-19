class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        leftP = [1] * n
        product = 1
        for i in range(n):
            leftP[i] = product
            product *= nums[i]
        
        rightP = [1] * n
        product = 1
        for i in range(n - 1, -1, -1):
            rightP[i] = product
            product *= nums[i]

        output = [1] * n
        for i in range(n):
            output[i] = leftP[i] * rightP[i]
        
        return output
