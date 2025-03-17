# pyright: basic

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels = set('aeiou')
        consonants = set('bcdfghjklmnpqrstvwxyz')
        valid_chars = set('1234567890') | vowels | consonants
        word_chars = set(word.lower())

        return \
            len(word) >= 3 \
            and word_chars.issubset(valid_chars) \
            and not word_chars.isdisjoint(vowels) \
            and not word_chars.isdisjoint(consonants) \

