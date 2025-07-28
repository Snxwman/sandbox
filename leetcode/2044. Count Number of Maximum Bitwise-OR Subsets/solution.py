class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        subset_ors: list[int] = [0]

        for num in nums:
            for i in range(len(subset_ors)):
                val = subset_ors[i] | num
                subset_ors.append(val)

        return subset_ors.count(max(subset_ors))

    def countMaxOrSubsets_2(self, nums: list[int]) -> int:
        max_or = 0
        subset_ors: list[int] = [0]

        for num in nums:
            max_or |= num

        for num in nums:
            for i in range(len(subset_ors)):
                val = subset_ors[i] | num
                subset_ors.append(val)

        return subset_ors.count(max_or)

    def countMaxOrSubsets_3(self, nums: list[int]) -> int:
        def subset_or(vals: list[int]) -> int:
            res = 0
            for val in vals:
                res |= val
            return res

        max_or = subset_or(nums)
        subsets: list[list[int]] = [[]]

        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])

        count = 0
        for subset in subsets:
            if subset_or(subset) == max_or:
                count += 1

        return count
        
