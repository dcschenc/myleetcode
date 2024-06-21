class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp

        # for i in range(n+1):
        # #     print(i)
        #     b = bin(i)
        #     # print(b)
        #     for c in b[2:]:
        #         if c == '1':
        #             ans[i]+=1
        # return ans