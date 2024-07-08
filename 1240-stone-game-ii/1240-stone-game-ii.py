class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dfs(i, m):
            # If we can take all remaining piles, return the sum of those piles.
            if m * 2 >= n - i:
                return prefix_sums[n] - prefix_sums[i]
          
            # Try every possible number of stones we can take, and choose the option
            # that maximizes our stones.
            return max(
                prefix_sums[n] - prefix_sums[i] - dfs(i + x, max(m, x))
                for x in range(1, 2 * m + 1)
            )

        n = len(piles)  # The total number of piles.
        prefix_sums = list(accumulate(piles, initial=0))  # Prefix sum array to calculate the sum efficiently.
      
        # Start the game from the first pile, with the initial maximum of 1 stone to take.
        return dfs(0, 1)

        # n = len(piles)
        # dp = [[0 for j in range(n + 1)] for i in range(n)]
        # cur_sum = 0
        # for i in range(n-1, -1, -1):
        #     cur_sum += piles[i]
        #     for m in range(1, n + 1):
        #         if i + 2 * m >= n: 
        #             dp[i][m] = cur_sum
        #         else:
        #             for x in range(1, 2*m + 1):
        #                 dp[i][m] = max(dp[i][m], cur_sum - dp[i+x][max(x, m)])
        # return dp[0][1]


        