class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        leftP = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            leftP[i] = product
            product *= nums[i]
        
        rightP = [1] * len(nums)
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            rightP[i] = product
            product *= nums[i]

        output = [1] * len(nums)
        for i in range(len(nums)):
            output[i] = leftP[i] * rightP[i]
        
        return output
