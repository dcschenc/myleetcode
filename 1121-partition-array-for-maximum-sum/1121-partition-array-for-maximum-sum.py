class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1043.Partition%20Array%20for%20Maximum%20Sum
        # Length of the given array
        array_length = len(arr)
      
        # Initialize the dp (dynamic programming) array with 0's, 
        # where dp[i] will be the max sum for the subarray arr[0:i]
        dp = [0] * (array_length + 1)
      
        # Start from the first element and compute the max sum for each subarray
        for i in range(1, array_length + 1):
            max_element = 0  # To keep track of the maximum element in the current partition
          
            # Check partitions of lengths from 1 to k
            for j in range(i, max(0, i - k), -1):
              
                # Update the maximum element in the current partition
                max_element = max(max_element, arr[j - 1])
              
                # Update the dp table:
                # dp[i] is the maximum of its previous value and the sum of the new partition
                # The new partition sum is calculated by multiplying the size of the partition
                # (i - j + 1) with the maximum element in that partition.
                dp[i] = max(dp[i], dp[j - 1] + max_element * (i - j + 1))
      
        # Return the maximum sum for the entire array
        return dp[array_length]
        
        # n = len(arr)
        # dp = [0] * (n + 1)
        # for i in range(1, n + 1):
        #     mx = 0
        #     for j in range(i, max(0, i - k), -1):
        #         mx = max(mx, arr[j - 1])
        #         dp[i] = max(dp[i], dp[j - 1] + mx * (i - j + 1))
        # return dp[n]


        # def dp(idx, steps):
        #     if steps == k:
        #         return max(arr[idx:]) * len(arr[idx:])
        #     max_sum = 0
        #     for j in range(idx, n):
        #         if n - (j + 1) == k - steps: break
        #         cur = max(arr[idx:j+1]) * len(arr[idx:j+1]) + dp(j + 1, steps + 1)
        #         if max_sum <= cur:
        #             max_sum = cur
        #     return max_sum
        
        # n = len(arr)
        # ans = dp(0, 1)
        # return ans

        # n = len(arr)
        # dp = [[0 for j in range(n)] for i in range(k+1) ]
        # for i in range(1, k+1):
        #     for j in range(n - (k - i)):
        #         dp[i][j]