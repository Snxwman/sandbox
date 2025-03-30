class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                seq_len = 1

                next_num = num + 1
                while next_num in num_set:
                    seq_len += 1
                    next_num += 1

                longest = max(longest, seq_len)

        return longest


    def longestConsecutive_2(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        seqs: dict[int, int] = {}

        for num in num_set:
            if num - 1 not in num_set:
                seqs[num] = 1
                next_num = num + 1
                while next_num in num_set:
                    seqs[num] += 1
                    next_num += 1

        return max(seqs.values())
