class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        @cache
        def dfs(i: int, k: int) -> float:
            if i == n:
                return 0
            if k == 1:
                return (s[n] - s[i]) / (n - i)
            ans = 0
            for j in range(i + 1, n):
                ans = max(ans, (s[j] - s[i]) / (j - i) + dfs(j, k - 1))
            return ans

        n = len(nums)
        s = list(accumulate(nums, initial=0))
        return dfs(0, k)

        
        @functools.lru_cache(None)
        def dfs(i, k):
            if k == 1: 
                return sum(nums[i:])/len(nums[i:])                 
            maxAvg = 0
            # Try paritioning at each index and calculate average
            for j in range(i+1, len(nums)): 
                avg = sum(nums[i:j])/len(nums[i:j])
                # Call with the next index (j) after partition
                subarrayAvg = avg + dfs(j, k-1) 
                maxAvg = max(maxAvg, subarrayAvg)
            return maxAvg

        return dfs(0, k)

        # n = len(nums)
        # prefix_sum = [0] * (n + 1)

        # for i in range(n):
        #     prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # dp = [0] * n

        # for i in range(n):
        #     dp[i] = prefix_sum[i + 1] / (i + 1)

        # for group in range(2, k + 1):
        #     new_dp = [0] * n

        #     for i in range(n):
        #         for j in range(i):
        #             new_dp[i] = max(new_dp[i], dp[j] + (prefix_sum[i + 1] - prefix_sum[j + 1]) / (i - j))

        #     dp = new_dp

        # return dp[-1]