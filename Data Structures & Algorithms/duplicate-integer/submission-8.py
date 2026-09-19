class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dupes = set()

        for idx in range(len(nums)):
            if nums[idx] in dupes:
                return True
            else:
                dupes.add(nums[idx])

        return False