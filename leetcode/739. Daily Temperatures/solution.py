class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack: list[tuple[int, int]] = []  # (temp, index)
        answer: list[int] = [0] * len(temperatures)

        for this_day, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, last_day = stack.pop()
                answer[last_day] = this_day - last_day

            stack.append((temp, this_day))

        return answer

    def dailyTemperatures_2(self, temperatures: list[int]) -> list[int]:
        stack: list[int] = []  # (temp, index)
        answer: list[int] = [0] * len(temperatures)

        for this_day in range(len(temperatures)):
            while stack and temperatures[this_day] > temperatures[stack[-1]]:
                last_day = stack.pop()
                answer[last_day] = this_day - last_day

            stack.append(this_day)

        return answer
