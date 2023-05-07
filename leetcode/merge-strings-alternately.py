# source: https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(max(len(word1), len(word2))):
            if i > len(word1) - 1:
                result += word2[i]
            elif i > len(word2) - 1:
                result += word1[i]
            else:
                result += f"{word1[i]}{word2[i]}"

        return result
