from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:       
        hm = defaultdict(int)
        n, i = len(s), 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            num = j - i
            for l in range(1, num+1):
                key = s[i] * l
                hm[key] += num - l + 1     
            i = j
        ans = [len(k) for k, v in hm.items() if v >=3]
        ans.sort(reverse=True)
        return ans[0] if ans else -1
        
        # hm = defaultdict(int)
        # n = len(s)
        # i = 1
        # hm[s[0]] = 1
        # prev = 0
        # while i < n:
        #     if s[i] == s[i-1]:
        #         for j in range(prev, i+1):
        #             hm[s[j:i+1]] += 1
        #     else:
        #         prev = i
        #         hm[s[i]] += 1
        #     i += 1
        # ans = [len(k) for k, v in hm.items() if v >=3]
        # ans.sort(reverse=True)
        # return ans[0] if ans else -1


        # for i in range(n):
        #     hm[s[i]] += 1
        #     cur = s[i]
        #     for j in range(i+1, n):
        #         if s[j] != s[j-1]:
        #             break
        #         cur += s[j]
        #         hm[cur] += 1
        # ans = [len(k) for k, v in hm.items() if v >= 3]
        # ans.sort(reverse=True)
        # return ans[0] if ans else -1