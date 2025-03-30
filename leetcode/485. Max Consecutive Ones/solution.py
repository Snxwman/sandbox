class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_con, cur_con = 0, 0

        for num in nums:
            if num == 1:
                cur_con += 1
            else:
                # Only check for new max when the current run ends
                max_con = max_con if max_con > cur_con else cur_con
                cur_con = 0

        # If the last number is a one, max_con might not get reset
        return max(max_con, cur_con)


    def findMaxConsecutiveOnes_2(self, nums: list[int]) -> int:
        max_con = 0
        cur_con = 0

        for num in nums:
            if num == 1:
                cur_con += 1
                if cur_con > max_con:
                    max_con = cur_con
            else:
                cur_con = 0

        return max_con


    def findMaxConsecutiveOnes_3(self, nums: list[int]) -> int:
        max_con = 0
        win_size = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                win_size += 1
                max_con = max(max_con, win_size)
            else:
                win_size = 0

        return max_con
