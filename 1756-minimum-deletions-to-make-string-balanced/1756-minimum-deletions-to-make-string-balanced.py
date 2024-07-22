class Solution:
    def minimumDeletions(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1653.Minimum%20Deletions%20to%20Make%20String%20Balanced
        n = len(s)
        dp = [0] * (n + 1)
        b = 0
        for i, c in enumerate(s, 1):
            if c == 'b':
                dp[i] = dp[i - 1]
                b += 1
            else:
                dp[i] = min(dp[i - 1] + 1, b)
        return dp[n]

        n = len(s)
        rightDel = s.count('a')
        leftDel = 0
        ans = rightDel
        for i in range(len(s)):
            if s[i] == 'b':
                leftDel += 1
            else:
                rightDel -= 1
                ans = min(ans, leftDel + rightDel)
        return ans


        # presum = [0] * n
        # postsum = [0] * n
        # if s[0] == 'b':
        #     presum[0] = 1
        # i = 1
        # while i < n:
        #     if s[i] == 'b':
        #         presum[i] = presum[i-1] + 1
        #     else:
        #         presum[i] = presum[i-1]
        #     i += 1
        
        # if s[-1] == 'a':
        #     postsum[n-1] = 1
        # i = n - 2
        # while i >= 0:       
        #     if s[i] == 'a':                
        #         postsum[i] = postsum[i+1] + 1
        #     else:
        #         postsum[i] = postsum[i+1]
        #     i -= 1
        # ans = float('inf')
        # for i in range(n):
        #     ans = min(ans, presum[i] + postsum[i] - 1)
        # return ans