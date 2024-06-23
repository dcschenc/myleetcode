class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ######### O(target_sum) #########
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        # Create a 1D list dp, where dp[i] represents if it's possible to form
        # a subset with a sum of i using the first n elements of the array.
        dp = [False] * (target_sum + 1)

        # Initialization: It's always possible to form a subset with a sum of 0.
        dp[0] = True

        # Fill the dp table using dynamic programming
        for num in nums:
            for j in range(target_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target_sum]

        ########  O(n * target_sum) ######
        total_sum = sum(nums)

        # If the total sum is odd, it cannot be partitioned into two equal subsets
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        # Create a 2D table dp[i][j] where dp[i][j] represents if it's possible to
        # form a subset with a sum of j using the first i elements of the array.
        dp = [[False] * (target_sum + 1) for _ in range(n + 1)]

        # Initialization: It's always possible to form a subset with a sum of 0.
        for i in range(n + 1):
            dp[i][0] = True

        # Fill the dp table using dynamic programming
        for i in range(1, n + 1):
            for j in range(1, target_sum + 1):
                # If the current element can be included in the subset, check if
                # it's possible to form a subset with the remaining elements.
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]

        # The final value in dp[n][target_sum] will indicate if it's possible to
        # partition the array into two equal subsets.
        return dp[n][target_sum]

        # total = sum(nums)
        # if total%2 != 0:
        #     return False
        # target = total//2
        # dp = [0] * (target + 1)
        # for i in range(len(nums)):
        #     for j in range(target,nums[i]-1,-1):
        #         dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
        # return dp[target] == target



        # if len(nums) < 2:
        #     return False
        # nums.sort()
        # L, R = 0, len(nums) - 1
        # LSum, RSum = nums[L], nums[R]
        # print(nums)
        # while L < R:                     
        #     if LSum < RSum:
        #         L += 1
        #         LSum += nums[L]
        #     elif LSum > RSum:
        #         R -= 1
        #         RSum += nums[R]
        #     else:
        #         if L == R - 1:
        #             return True
        #         elif L + 1 == R - 1:
        #             return False
        #         else:
        #             L += 1
        #             LSum += nums[L]
        #             R -= 1
        #             RSum += nums[R]
        # print(L,R,LSum,RSum)
        # return LSum == RSum

