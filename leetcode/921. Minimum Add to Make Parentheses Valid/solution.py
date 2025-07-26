class Solution:
    def minAddToMakeValid_1(self, s: str) -> int:
        # Using stack, O(n) time, O(n) space
        stack: list[str] = []

        for char in s:
            if char == '(':
                stack.append(char)
            else:
                if len(stack) != 0 and stack[-1] == '(':
                    _ = stack.pop()
                else:
                    stack.append(char)

        return len(stack)

    def minAddToMakeValid_2(self, s: str) -> int:
        # Using counters, O(n) time, O(1) space
        unopened, unclosed = 0, 0

        for char in s:
            if char == '(':
                unclosed += 1
            else:
                if unclosed > 0:
                    unclosed -= 1
                else:
                    unopened += 1

        return unopened + unclosed
               
