class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        total = 0
        for i in range(n):           
            for j in range(i + 1, n + 1):
                if s[i:j].count('0') <= k or s[i:j].count('1') <= k:
                    total += 1
                
        return total