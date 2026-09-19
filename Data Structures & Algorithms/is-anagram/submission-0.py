class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge cases
        if len(s) != len(t): return False

        letterCount = dict()
        for x in s: # O(n)
            if x in letterCount.keys():
                letterCount[x] = letterCount.get(x, 0) + 1 
            else:
                letterCount[x] = 1

        for y in t: # O(n)
            letterCount[y] = letterCount.get(y, 0) - 1

        for count in letterCount.values(): # O(n)
            if count != 0:
                return False
        
        return True

        # Time complexity: O(n)
        # Space complexity: O(n)