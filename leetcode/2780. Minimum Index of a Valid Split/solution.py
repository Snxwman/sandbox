from collections import defaultdict


class Solution:
    def minimumIndex_1(self, nums: list[int]) -> int:
        n = len(nums)

        candidate = nums[0]
        candidate_count = 0
        for num in nums:
            if num == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1

            if candidate_count == 0:
                candidate = num
                candidate_count = 1
        
        dominant = candidate
        dominant_count = 0
        for num in nums:
            if num == dominant:
                dominant_count += 1

        left_count = 0
        for i in range(n):
            if nums[i] == dominant:
                left_count += 1

            right_count = dominant_count - left_count

            if left_count*2 > i+1 and right_count*2 > n-i-1:
                return i

        return -1


    def minimumIndex_2(self, nums: list[int]) -> int:
        left = defaultdict(int)
        right = defaultdict(int)
        n = len(nums)

        for num in nums:
            right[num] += 1

        for i in range(n):
            num = nums[i]
            left[num] += 1
            right[num] -= 1

            if left[num]*2 > i+1 and right[num]*2 > n-i-1:
                return i

        return -1
        
