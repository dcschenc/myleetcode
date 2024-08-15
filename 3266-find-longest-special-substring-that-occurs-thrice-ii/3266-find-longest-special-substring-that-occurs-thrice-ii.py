class Solution:
    def maximumLength(self, s: str) -> int:
        # https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-ii/solutions/4507971/python-sliding-window-hashmap/        
        hm = defaultdict(int)        
        start = 0
        while start < len(s):
            cur = start
            while cur < len(s) - 1 and s[cur] == s[cur + 1]:
                cur += 1
            window_size = cur + 1 - start
            for length in range(1, window_size + 1):
                hm[(s[start], length)] += window_size + 1 - length                
            start = cur + 1

        res = -1
        for k in hm:
            if hm[k] >= 3:
                res = max(res, k[1])                
        return res

        def check(x: int) -> bool:
            cnt = defaultdict(int)
            i = 0
            while i < n:
                j = i + 1
                while j < n and s[j] == s[i]:
                    j += 1
                cnt[s[i]] += max(0, j - i - x + 1)
                i = j
            return max(cnt.values()) >= 3

        n = len(s)
        l, r = 0, n
        while l < r:
            mid = (l + r + 1) >> 1
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return -1 if l == 0 else l

        hm = defaultdict(int)
        n, i, l = len(s), 1, 0
        hm[s[0]] += 1
        while i < n:
            if s[i] != s[i-1]:
                l = i
            for k in range(l, i+1):
                hm[s[l:k+1]] += 1
            i += 1
        mx = -1
        for k, v in hm.items():
            if v >= 3:
                mx = max(mx, len(k))
        return mx

        