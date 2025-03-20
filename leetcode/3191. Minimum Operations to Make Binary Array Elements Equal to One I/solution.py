class Solution:
    def minOperations_1(self, nums: list[int]) -> int:
        # 83ms
        ops = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                ops += 1

        return ops if nums[-2] == 1 and nums[-1] == 1 else -1


    def minOperations_2(self, nums: list[int]) -> int:
        # 103ms
        ops = 0
        n = len(nums)
        i = 0

        while i+3 <= n:
            if nums[i] == 0:
                ops += 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1

                if nums[i+1] == 1 and nums[i+2] == 1:
                    if nums[i+2] == 1:
                        i += 3
                    else:
                        i += 2
                    continue
            i += 1 

        return ops if nums[-2] == 1 and nums[-1] == 1 else -1


    def minOperations_3(self, nums: list[int]) -> int:
        # 122ms
        ops = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i+0] = nums[i+0] ^ 1
                nums[i+1] = nums[i+1] ^ 1
                nums[i+2] = nums[i+2] ^ 1
                ops += 1

        return -1 if nums[-1] == 0 or nums[-2] == 0 or nums[-3] == 0 else ops


    def minOperations_4(self, nums: list[int]) -> int:
        # 317ms
        ops = 0

        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i:i+3] = map(lambda bit: bit ^ 1, nums[i:i+3])
                ops += 1

        return ops if all(nums) else -1

