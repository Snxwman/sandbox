class Solution:
    def removeStars(self, s: str) -> str:
        stack: list[str] = []
        for c in s:
            stack.pop() if c == '*' else stack.append(c)

        return ''.join(stack)


    def removeStars_2(self, s: str) -> str:
        stack: list[str] = []
        for c in s:
            if c == '*':
                _ = stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)
