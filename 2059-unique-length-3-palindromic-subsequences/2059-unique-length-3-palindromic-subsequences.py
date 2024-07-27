class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in ascii_lowercase:
            l, r = s.find(c), s.rfind(c)
            if r - l > 1:
                ans += len(set(s[l + 1 : r]))
        return ans
        
        pairs = set()
        n = len(s)
        pre = [set()] * n
        for i, c in enumerate(s):
            if i > 0:
                pre[i] = pre[i-1].copy()
            pre[i].add(c)
        
        post = [set()] * n
        for i in range(n-1, -1, -1):
            if i < n - 1:
                post[i] = post[i + 1].copy()
            post[i].add(s[i])        

        for i in range(1, n-1):
            for c in pre[i-1]:
                if c in post[i+1]:
                    pairs.add((c, s[i], c))        
        return len(pairs)