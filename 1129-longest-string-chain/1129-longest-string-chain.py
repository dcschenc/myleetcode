# from collections import defaultdict
class Solution:
    def longestStrChain(self, words: List[str]) -> int:        
        def check(w1, w2):
            if len(w2) - len(w1) != 1:
                return False
            i = j = cnt = 0
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    cnt += 1
                else:
                    i += 1
                j += 1
            return cnt < 2 and i == len(w1)

        n = len(words)
        dp = [1] * (n + 1)
        words.sort(key=lambda x: len(x))
        res = 1
        for i in range(1, n):
            for j in range(i):
                if check(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
            res = max(res, dp[i])
        return res


        # @cache
        # def can_continue(w1, w2):
        #     i, j = 0, 0
        #     while i < len(w1) and j < len(w2):
        #         if w1[i] == w2[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j += 1
        #     return i == len(w1)
            
        # @cache
        # def dfs(w1, cnt):           
        #     ans = cnt
        #     length = len(w1)
        #     length = length + 1
        #     for w2 in hm[length]:
        #         if can_continue(w1, w2):
        #             ans = max(ans, dfs(w2, cnt+1))
                    
        #     return ans   

        # hm = defaultdict(list)
        # for w in words:
        #     hm[len(w)].append(w)
        # sorted_items = sorted(hm.items(), key=lambda x: x[0])        
        # res = 0
        # for k, v in sorted_items:
        #     for w1 in v:
        #         res = max(res, dfs(w1, 1))
        # return res
        