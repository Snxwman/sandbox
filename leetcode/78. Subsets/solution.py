class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        # Cascading approach
        subsets: list[list[int]] = [[]]

        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])

        return subsets

    def subsets_2(self, nums: list[int]) -> list[list[int]]:
        # Backtracking approach
        subsets: list[list[int]] = []

        def backtrack(start: int, subset: list[int]):
            subsets.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                _ = subset.pop()

        backtrack(0, [])
        return subsets
