class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        parMap = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in parMap:
                # Pop
                if stack and stack[-1] == parMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                # Push
                stack.append(c)

        return len(stack) == 0
