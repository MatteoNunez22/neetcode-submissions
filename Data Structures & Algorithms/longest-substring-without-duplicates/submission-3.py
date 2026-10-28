class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l, r = 0, 0
        maxL = 1
        set_s = set()
        while r < len(s):
            if s[r] not in set_s:
                # Valid substring
                set_s.add(s[r])
                maxL = max(maxL, len(set_s))
                r += 1
            else:
                set_s.remove(s[l])
                l += 1

        return maxL