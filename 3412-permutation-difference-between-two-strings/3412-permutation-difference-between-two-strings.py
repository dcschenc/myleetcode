class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        total = 0
        for i, c1 in enumerate(s):
            for j, c2 in enumerate(t):
                if c1 == c2:
                    total += abs(i-j)
        return total