class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        slow, fast = 0, 0
        while fast < n:
            while slow < n and nums[slow] != 0:
                slow += 1

            if fast < slow:
                fast = slow + 1

            while fast < n and nums[fast] == 0:
                fast += 1

            if fast < n:
                nums[slow] = nums[fast]
                nums[fast] = 0
