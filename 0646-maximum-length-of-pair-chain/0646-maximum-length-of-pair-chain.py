class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)
        for i, (c, _) in enumerate(pairs):
            for j, (_, b) in enumerate(pairs[:i]):
                if b < c:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        

        # n = len(pairs)
        # pairs.sort()
        # dp = [1 for i in range(n)]
        # for i in range(1, n):
        #     for j in range(i-1, -1, -1):
        #         if pairs[i][0] > pairs[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #             break
        # return dp[n-1]

        # @cache
        # def dp(right, i):
        #     res = 0
        #     for j in range(i, n):                
        #         if pairs[j][0] > right:
        #            res = max(res, 1 +  dp(pairs[j][1], j + 1))
        #     return res

        # n = len(pairs)
        # pairs.sort()
        # ans = [0]
        # for i, (l, r) in enumerate(pairs):
        #     ans[0] = max(ans[0], 1 + dp(r, i + 1))
        # return ans[0]