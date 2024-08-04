class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2369.Check%20if%20There%20is%20a%20Valid%20Partition%20For%20The%20Array
        @cache
        def dfs(i: int) -> bool:
            if i >= n:
                return True
            ans = False
            if i + 1 < n and nums[i] == nums[i + 1]:
                ans |= dfs(i + 2)
            if i + 2 < n:
                if nums[i] == nums[i + 1] == nums[i + 2] or \
                    nums[i + 1] - nums[i] == 1 and nums[i + 2] - nums[i + 1] == 1:
                    ans |= dfs(i + 3)
            return ans

        n = len(nums)
        return dfs(0)

        n = len(nums)
        dp = [True] + [False] * n

        # Determine if the prefix array nums[0 ~ i] has a valid partition
        for i in range(n):
            dp_index = i + 1

            # Check 3 possibilities
            if i > 0 and nums[i] == nums[i - 1]:
                dp[dp_index] |= dp[dp_index - 2]
            if i > 1 and nums[i] == nums[i - 1] == nums[i - 2]:
                dp[dp_index] |= dp[dp_index - 3]
            if i > 1 and nums[i] == nums[i - 1] + 1 == nums[i - 2] + 2:
                dp[dp_index] |= dp[dp_index - 3]
 
        return dp[n]

        # i, n = 1, len(nums)
        # dp = [False] * (n + 1)
        # dp[0] = True
        # if nums[0] == nums[1]:
        #     dp[1] = True
        # for i in range(2, n+1):           
        #     if len(set(nums[i-2:i])) == 1:
        #         dp[i] = dp[i] | dp[i-2]
        #     if i - 3 >= 2 or i - 3 == 0:
        #         if len(set(nums[i-3:i])) == 1:
        #             dp[i] = dp[i] | dp[i-3]
        #         if nums[i-3] + 1 == nums[i-2]  and nums[i-2] + 1 == nums[i-1]:
        #             dp[i] = dp[i] | dp[i-3]
        # return dp[n]

