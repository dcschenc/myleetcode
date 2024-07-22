class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # https://leetcode.com/problems/maximum-repeating-substring/
        for k in range(len(sequence) // len(word), -1, -1):
            if word * k in sequence:
                return k
        return -1

        k = 0
        for i in range(1, len(sequence)//len(word)+1):
            if word * i not in sequence:
                return i-1
            k += 1   
        return k