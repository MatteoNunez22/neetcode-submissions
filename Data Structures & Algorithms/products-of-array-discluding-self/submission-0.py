class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalP = 1
        zeroCount = 0
        zeroIdx = -1
        for i in range(len(nums)):
            if nums[i] != 0:
                totalP *= nums[i]
            else:
                zeroCount += 1
                zeroIdx = i
        
        output = [0] * len(nums)

        if zeroCount == 0:
            for i in range(len(output)):
                output[i] = int(totalP / nums[i])
        elif zeroCount == 1:
            output[zeroIdx] = totalP

        return output
