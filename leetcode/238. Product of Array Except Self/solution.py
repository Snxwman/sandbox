# pyright: basic

class Solution(object):
    def productExceptSelf_3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zero_count = nums.count(0)

        # When more than 1 zero is in nums, product is always 0
        if zero_count > 1:
            return [0] * len(nums)

        # When exactly 1 zero is in nums, all products except the nums.index(0) product are 0
        if zero_count == 1:
            zero_index = nums.index(0)
            product = [0] * len(nums)
            product[zero_index] = 1
            for num in nums:
                if num != 0:
                    product[zero_index] *= num
                else:
                    continue
            return product

        # No zeros in nums
        n = len(nums) 
        # Initialize product with all 1s
        # Each product[i] = prefix[i] * suffix[i]
        # Build product in place below
        product = [1] * n

        # Calculate running prefix, store prefix[i] in product[i]
        prefix = 1
        for i in range(1, n):  # skip i=0, prefix[0] is always 1, product already initialized as 1
            prefix *= nums[i-1]
            product[i] = prefix

        # Calculate running suffix, multiply product[i] (currently == prefix[i]) by suffix[i]
        suffix = 1
        for i in range(n-2, -1, -1):  # skip i=(n-1), suffix[-1] is always 1, suffix already initialized as 1s
            suffix *= nums[i+1]
            product[i] *= suffix

        return product


    def productExceptSelf_2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(1, n):
            prefix *= nums[i-1]
            ans[i] *= prefix

        suffix = 1
        for i in range(n-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix

        return ans


    def productExceptSelf_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        prefix = [1] + [0] * (n-1)
        suffix = [0] * (n-1) + [1]

        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = nums[i+1] * suffix[i+1]

        return [prefix[i]*suffix[i] for i in range(0,n)]
