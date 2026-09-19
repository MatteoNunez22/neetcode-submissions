class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            a = s[i]
            b = s[j]
            if not a.isalnum():
                i += 1
            elif not b.isalnum():
                j -= 1
            elif a.lower() != b.lower():
                return False
            else:
                i += 1
                j -= 1
        
        return True
