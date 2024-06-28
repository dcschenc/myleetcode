class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        i, n = 0, len(s)
        ans = []
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            if j - i >= 3:
                ans.append([i, j - 1])
            i = j
        return ans
        
        res = []
        start = 0
        for i in range(1,len(s)):
            if s[i] != s[start]:
                if i - start >= 3:
                    res.append([start, i-1])
                start = i
            elif i == len(s) - 1:
                if i - start + 1 >=3:
                    res.append([start, i])
            
        return res
            