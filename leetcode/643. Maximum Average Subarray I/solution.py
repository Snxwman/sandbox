class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur_sum = sum(nums[0:k])
        max_sum = cur_sum

        for i in range(k, len(nums)):
            cur_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, cur_sum)

        return max_sum / k


    def findMaxAverage_2(self, nums: list[int], k: int) -> float:
        n = len(nums)
        last_sum = sum(nums[0:k])
        max_sum = last_sum
        max_avg = max_sum / k

        i = 1
        while i+k <= n:
            this_sum = last_sum - nums[i-1] + nums[i+k-1]
            if this_sum > max_sum:
                max_sum = this_sum
                max_avg = max_sum / k

            last_sum = this_sum
            i += 1

        return max_avg

