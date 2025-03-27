class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        def find_cuts(rectangles: list[list[int]], i: int) -> bool:
            rectangles.sort(key=lambda r: r[i])

            cuts = 0
            end = 1
            for rect in rectangles:
                if rect[i] >= end:
                    cuts += 1
                end = max(end, rect[i+2])

            return cuts >= 2

        return find_cuts(rectangles, 0) or find_cuts(rectangles, 1)

