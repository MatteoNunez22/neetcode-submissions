class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = (0, 0)
        mp = {}
        maxLength = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(l, mp[s[r]] + 1)
            mp[s[r]] = r
            maxLength = max(maxLength, r - l + 1)

        return maxLength