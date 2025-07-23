class Solution:
    def maximumGain_1(self, s: str, x: int, y: int) -> int:
        points = 0
        remaining = s

        prio_str, prio_val, other_str, other_val = (
            ('ab', x, 'ba', y) if x > y else ('ba', y, 'ab', x)
        )

        def remove_all(target: str, val: int):
            nonlocal remaining, points
            stack = []

            for char in remaining:
                if len(stack) > 0 and stack[-1] + char == target:
                    _ = stack.pop()
                    points += val
                else:
                    stack.append(char)

            remaining = ''.join(stack)

        remove_all(prio_str, prio_val)
        remove_all(other_str, other_val)

        return points

    def maximumGain_2(self, s: str, x: int, y: int) -> int:
        points = 0
        remaining: str = s

        prio_str, prio_val, other_str, other_val = (
            ('ab', x, 'ba', y) if x > y else ('ba', y, 'ab', x)
        )

        def remove_all(target: str, val: int):
            nonlocal remaining, points

            for i in range(len(remaining)-1, -1, -1):
                if remaining[i:i+2] == target:
                    remaining = remaining[:i] + remaining[i+2:]
                    points += val

        remove_all(prio_str, prio_val)
        remove_all(other_str, other_val)

        return points
