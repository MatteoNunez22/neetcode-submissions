class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        maxLength = 0

        for num in setNums:
            if (num - 1) not in setNums:
                length = 1
                n = num + 1
                while n in setNums:
                    n += 1
                    length += 1
                maxLength = max(maxLength, length)

        return maxLength