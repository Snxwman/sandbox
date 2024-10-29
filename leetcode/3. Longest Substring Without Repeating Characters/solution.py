class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idx = 0
        width = 0

        while idx + width < len(s):
            window = set(s[idx : idx+width])

            if width != len(window):
                idx += 1
                continue

            if s[idx + width] not in window:
                width += 1
            else:
                idx += 1

        return width
        

