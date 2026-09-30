class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]

        stack = []
        for token in tokens:
            if token in operands:
                # Pop
                top = stack.pop()
                bot = stack.pop()
                if token == "+":
                    res = bot + top
                elif token == "-":
                    res = bot - top
                elif token == "*":
                    res = bot * top
                else:
                    res = bot / top
                stack.append(int(res))
            else:
                # Push
                stack.append(int(token))
        
        return stack.pop()
