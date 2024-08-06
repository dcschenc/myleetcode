class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2486.Append%20Characters%20to%20String%20to%20Make%20Subsequence
        m, n = len(s), len(t)
        i, j = 0, 0
        for i in range(n):
            while j < m and t[i] != s[j]:
                j += 1
            if j == m:
                return n - i       
            j += 1 
        return  0

        # hm = defaultdict(deque)
        # for i, c in enumerate(s):
        #     hm[c].append(i)
            
        # prev = -1
        # for i, c in enumerate(t):
        #     if len(hm[c]) == 0 or prev != -1 and hm[c][-1] <= prev:
        #         return len(t) - i
        #     else:
        #         if prev == -1:
        #             prev = hm[c][0]
        #             hm[c].popleft()
        #         else:
        #             # mid = bisect_left(hm[c], x=prev)
        #             while prev >= hm[c][0]:
        #                 hm[c].popleft()
        # return 0

        # hm = {}
        # for i, c in enumerate(s):
        #     if c not in hm:
        #         hm[c] = i
        # prev = -1
        # for i, c in enumerate(t):
        #     if c not in hm or prev != -1 and hm[c] <= prev:
        #         return len(t) - i
        #     else:
        #         prev = hm[c]
        # return 0