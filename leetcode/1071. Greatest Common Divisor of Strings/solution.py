from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        return str1[:gcd(len(str1), len(str2))]


    def gcdOfStrings_2(self, str1: str, str2: str) -> str:
        str1_len, str2_len = len(str1), len(str2)

        def divides(size: int) -> bool:
            if str1_len % size != 0 or str2_len % size != 0:
                return False

            str1_multiple, str2_multiple = str1_len // size, str2_len // size
            substr = str1[:size]

            return substr * str1_multiple == str1 and substr * str2_multiple == str2

        for size in range(min(str1_len, str2_len), 0, -1):
            if divides(size):
                return str1[:size]

        return ''


    def gcdOfStrings_3(self, str1: str, str2: str) -> str:
        longest = str1 if len(str1) >= len(str2) else str2
        shortest = str1 if len(str1) < len(str2) else str2
        long_len = len(longest)
        short_len = len(shortest)

        if longest[0:short_len] != shortest:
            return ''

        window_size = short_len
        while window_size > 0:
            if long_len % window_size != 0 or short_len % window_size != 0:
                window_size -= 1
                continue

            long_subs = set([longest[i:i+window_size] for i in range(0, long_len, window_size)])
            short_subs = set([shortest[i:i+window_size] for i in range(0, short_len, window_size)])
            if len(long_subs) == 1 and len(short_subs) == 1:
                return longest[0:window_size]

            window_size -= 1

        return ''
