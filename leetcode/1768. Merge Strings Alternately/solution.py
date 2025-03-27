class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = min(len(word1), len(word2))
        rest = word1[shortest:] if len(word1) > len(word2) else word2[shortest:]

        merged = ""
        for i in range(0, shortest):
            merged += word1[i]
            merged += word2[i]

        return merged + rest

