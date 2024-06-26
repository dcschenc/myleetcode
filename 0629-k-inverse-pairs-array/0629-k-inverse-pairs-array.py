class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # # https://algo.monster/liteproblems/629
        # mod = 10**9 + 7  # Define the modulus value to keep numbers within integer bounds
      
        # # dp table representing the count of inverse pairs for the current number of integers
        # dp = [1] + [0] * k  
      
        # # Prefix sum array for optimization of the inner loop. The size is k+2 for 1-indexed and ease of access
        # prefix_sum = [0] * (k + 2)
      
        # # Iterate through integers from 1 to n
        # for current_number in range(1, n + 1):
        #     # Going through all possible counts of inverse pairs from 1 to k
        #     for inverse_count in range(1, k + 1):
        #         # Update the dp table by taking the count from the prefix_sum within the range
        #         # The range corresponds to the valid inverse pair counts that can be formed with the current number
        #         dp[inverse_count] = (prefix_sum[inverse_count + 1] - 
        #                              prefix_sum[max(0, inverse_count - (current_number - 1))]) % mod
          
        #     # Updating prefix_sum based on the updated dp table
        #     for index in range(1, k + 2):
        #         prefix_sum[index] = (prefix_sum[index - 1] + dp[index - 1]) % mod
              
        # # Returning the number of ways to form k inverse pairs with n integers
        # return dp[k]

        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0629.K%20Inverse%20Pairs%20Array
        # https://leetcode.com/problems/k-inverse-pairs-array/solutions/4634349/recursive-solution-with-explanation-python-3/
        MOD = 10**9 + 7
        # Initialize a 2D array to store the DP results
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        # Base case: there is one way to arrange 0 elements with 0 inverse pairs
        dp[0][0] = 1

        for i in range(1, n + 1):
            # Calculate the cumulative sum for the current row
            prefix_sum = [0] * (k + 1)
            prefix_sum[0] = dp[i - 1][0]
            for j in range(1, k + 1):
                prefix_sum[j] = (prefix_sum[j - 1] + dp[i - 1][j]) % MOD

            for j in range(k + 1):  ### 上一行的数目
                # Calculate the number of inverse pairs when adding the current element
                dp[i][j] = (prefix_sum[j] - (prefix_sum[j - i] if j >= i else 0)) % MOD

        return dp[n][k]

