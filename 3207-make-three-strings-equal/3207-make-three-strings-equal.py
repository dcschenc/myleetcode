class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        i, n = 0, min(len(s1), len(s2), len(s3))
        while i < n:
            if s1[i] == s2[i] == s3[i]:
                i += 1
            else:
                break
        return len(s1) + len(s2) + len(s3) - i * 3 if i != 0 else -1
