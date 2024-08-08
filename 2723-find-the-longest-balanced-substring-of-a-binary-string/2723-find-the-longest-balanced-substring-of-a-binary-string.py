class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i, mx = 0, 0
        while i < n:
            if s[i] == '0':
                zeroes = 1
                i += 1
                while i < n and s[i] == '0':
                    zeroes += 1
                    i += 1
                ones = 0
                while i < n and s[i] == '1':
                    ones += 1
                    i += 1               
                mx = max(mx, min(zeroes, ones) * 2)                
            else:
                i += 1
                
        return mx