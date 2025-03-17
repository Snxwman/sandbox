from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        idx = 0
        width = 0

        while idx + width < len(s):
            window = s[idx : idx+width+1]
            counter = Counter(window)

            k_needed = len(window) - window.count(counter.most_common(1)[0][0])
            if k_needed <= k:
                width += 1
            else:
                idx += 1

        return width
