class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        # Calculate the prefix sum array of the stones list
        prefix_sum = list(accumulate(stones))
      
        # Initialize the 'score' variable with the last value of the prefix sum,
        # which corresponds to the sum of all stones.
        score = prefix_sum[-1]
      
        # Reverse iterate over the prefix_sum array starting from the second last element
        # The loop goes till the second element as the first move can't use only one stone
        for i in range(len(stones) - 2, 0, -1):
            # Update the 'score' to be the maximum value between the current 'score'
            # and the difference between the current prefix_sum and the 'score'
            # This represents choosing the optimal score after each player's turn
            score = max(score, prefix_sum[i] - score)
      
        # Return the final score after both players have played optimally
        return score


        # # https://leetcode.com/problems/stone-game-viii/solutions/1224872/top-down-and-bottom-up/
        # @cache
        # def df(i: int) -> int:
        #     if i >= len(stones) - 1:
        #         return s[-1]
        #     return max(df(i + 1), s[i] - df(i + 1))

        # s = list(accumulate(stones))
        # return df(1)

        n = len(stones)
    
        # Compute prefix sums
        prefix_sums = [0] * n
        prefix_sums[0] = stones[0]
        for i in range(1, n):
            prefix_sums[i] = prefix_sums[i - 1] + stones[i]
        
        # Initialize dp array
        dp = [0] * n
        dp[-1] = prefix_sums[-1]
        
        # Fill dp array
        for i in range(n - 2, 0, -1):
            dp[i] = max(dp[i + 1], prefix_sums[i] - dp[i + 1])
        
        return dp[1]

