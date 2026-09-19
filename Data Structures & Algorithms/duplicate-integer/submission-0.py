class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Edge cases
        if len(nums) < 2:
            return False
        
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False