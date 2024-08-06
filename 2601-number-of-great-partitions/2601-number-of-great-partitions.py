class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2518.Number%20of%20Great%20Partitions
        # https://algo.monster/liteproblems/2514
        
        # Check if the total sum of nums is less than the double of k
        # In that case, there would be no way to partition the nums into k equal-sum parts
        if sum(nums) < k * 2:
            return 0

        # Define a modulus number for the result to prevent integer overflow
        mod = 10**9 + 7

        # Get the length of the nums list
        n = len(nums)

        # Initialize a 2D array to use for dynamic programming
        # Dimensions are (n+1) x k, and it will hold the number of ways to reach a certain sum
        dp = [[0] * k for _ in range(n + 1)]

        # Base case: There's one way to have a sum of 0 (with no elements)
        dp[0][0] = 1

        # Variable to store the answer
        ans = 1

        # Iterate over the range from 1 to n inclusive
        for i in range(1, n + 1):
            # Double the answer on each iteration
            ans = ans * 2 % mod

            for j in range(k):
                # Carry over the previous count for this sum
                dp[i][j] = dp[i - 1][j]

                # If the current number can be used to build up the sum
                if j >= nums[i - 1]:
                    # Add the number of ways to reach the sum without the current number
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - nums[i - 1]]) % mod
      
        # Use the final answers in dp to adjust the overall answer
        # Subtract twice the sum of all counts for partitions of size (k-1)
        # Adding mod before taking mod again for handling negative values
        return (ans - sum(dp[-1]) * 2 + mod) % mod

        @lru_cache(None)
        def dfs(i, x, y):
            if i > n: 
                return 0
            if i == n:
                if x >= k and y >= k:
                    return 1
                return 0
            ans = 0
            ans += dfs(i + 1, x + nums[i], y)
            ans += dfs(i + 1, x, y + nums[i])     
            return ans % mod

        n = len(nums)
        mod = 10 ** 9 + 7
        ans = dfs(0, 0, 0)
        dfs.cache_clear()
        return ans % mod        