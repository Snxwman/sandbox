class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        start, end, num_zeros, longest = 0, 0, 0, 0
        n = len(nums)

        while end < n:
            if nums[end] == 1:
                end += 1
            elif num_zeros < k:
                end += 1
                num_zeros += 1
            else:
                if nums[start] == 0:
                    num_zeros -= 1
                start += 1

            longest = max(longest, end - start)

        return longest


    def longestOnes_2(self, nums: list[int], k: int) -> int:
        start, size = 0, 0

        while start + size < len(nums):
            i = start + size
            if nums[i] == 1:
                size += 1
            elif nums[start:i+1].count(0) <= k:
                size += 1
            else:
                start += 1
                while nums[start:start+size].count(0) > k:
                    start += 1

        return size
