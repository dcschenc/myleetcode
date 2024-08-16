class Solution:
    def maximumLengthSubstring(self, s: str) -> int:        
        n = len(s)
        mx = 0
        for i in range(n):
            counter = Counter()
            for j in range(i, n):
                counter[s[j]] += 1
                if counter[s[j]] > 2:
                    break
                mx = max(mx, j - i + 1)
        return mx
