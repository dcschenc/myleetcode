class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        ans = [n] * n
        pre = -inf
        for i, ch in enumerate(s):
            if ch == c:
                pre = i
            ans[i] = min(ans[i], i - pre)
        suf = inf
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                suf = i
            ans[i] = min(ans[i], suf - i)
        return ans

#         Travelling front to back
        result = [len(s)] * len(s)
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[i] == s[j] == c:
                result[i] = 0
                i += 1
                j += 1
            elif s[i] != c and s[j] == c:
                result[i] = abs(i-j)
                i += 1
            elif s[i] != c and s[j] != c:
                j += 1
    
#         Travelling back to front
        i = j = len(s) - 1
        while i >= 0 and j >= 0:
            if s[i] == s[j] == c:
                result[i] = 0
                i -= 1
                j -= 1
            elif s[i] != c and s[j] == c:
                # if type(result[i]) == int:
                result[i] = min(result[i], abs(i-j))
                # else:
                    # result[i] = abs(i-j)
                i -= 1
            elif s[i] != c and s[j] != c:
                j -= 1
        
        return result