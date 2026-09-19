class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                print("Increase i: ", s[i])
                i += 1
            elif not s[j].isalnum():
                print("Increase j: ", s[j])
                j -= 1
            elif s[i].lower() != s[j].lower(): 
                print("Mismatch: ", s[i], s[j])
                return False
            else:
                print("Equal: ", s[i], s[j])
                i += 1
                j -= 1
        
        return True