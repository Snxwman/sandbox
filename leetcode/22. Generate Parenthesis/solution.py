class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parens: list[str] = []
        parens.append('(')  # Always the base case

        while not all(len(p) == 2 * n for p in parens):
            for i, partial in enumerate(parens):
                if len(partial) == 2 * n:
                    continue

                num_open = partial.count('(')
                num_closed = len(partial) - num_open

                if num_open == num_closed:
                    parens[i] = partial + '('
                elif num_open > num_closed:
                    if num_open < n:
                        parens.append(partial + ')')
                        parens[i] = partial + '('
                    else:
                        parens[i] = partial + ')'

        return parens

    def generateParenthesis_2(self, n: int) -> list[str]:
        stack: list[str] = []
        parens: list[str] = []

        def backtrack(num_open: int, num_closed: int) -> None:
            if num_open + num_closed == 2 * n:
                parens.append(''.join(stack))

            if num_open < n:
                stack.append('(')
                backtrack(num_open + 1, num_closed)
                _ = stack.pop()

            if num_open > num_closed:
                stack.append(')')
                backtrack(num_open, num_closed + 1)
                _ = stack.pop()

        backtrack(0, 0)
        return parens
