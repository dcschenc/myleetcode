class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i][0]: not used yet
        # dp[i][1]: used
        dp = [[0 for j in range(2)] for i in range(n+1)]        
        ans = 1
        for i in range(1, n+1):
            if nums[i-1] == 1:
                dp[i][0] = dp[i-1][0]+1
                dp[i][1] = dp[i-1][1]+1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0]+1
            ans = max(ans, dp[i][0], dp[i][1])
        return ans

        @lru_cache(None)
        def dfs(i, k, count):
            if i >= n: 
                return count

            if nums[i] == 0 and k <= 0: 
                return count

            max_cnt = 0

            if nums[i] == 1:
                max_cnt = max(max_cnt, dfs(i+1,k,count+1))

            if nums[i] == 0:
                max_cnt = max(max_cnt, dfs(i+1,k-1,count+1), dfs(i+1,k,0))

            return max_cnt

        n = len(nums)
        return dp(0,1,0)
