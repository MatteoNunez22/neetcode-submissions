class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(x, v) for x, v in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for x, v in pairs:
            t = (target - x) / v
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)