class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for a in range(len(nums)):
            if nums[a] > 0:
                break

            if a > 0 and nums[a - 1] == nums[a]:
                continue
            
            # Two sum
            b, c = a + 1, len(nums) - 1
            while b < c:
                threeSum = nums[a] + nums[b] + nums[c]
                
                if threeSum > 0:
                    c -= 1
                elif threeSum < 0:
                    b += 1
                else:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b - 1] == nums[b]:
                        b += 1

        return res