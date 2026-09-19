class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        l, r = (0, 0)
        window = set()

        while r < len(s):
            if s[r] not in window:
                window.add(s[r])
                r += 1
                maxLength = max(maxLength, r - l)
            else:
                window.remove(s[l])
                l += 1

        return maxLength