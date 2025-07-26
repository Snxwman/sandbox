class Solution:
    def reverseVowels(self, s: str) -> str:
        rev = list(s)
        vowels = 'aeiou'
        left, right = 0, len(s) - 1

        while left < right:
            while rev[left].lower() not in vowels and left < right:
                left += 1

            while rev[right].lower() not in vowels and left < right:
                right -= 1

            rev[left], rev[right] = rev[right], rev[left]
            left, right = left + 1, right - 1

        return ''.join(rev)
