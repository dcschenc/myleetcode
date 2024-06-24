class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dp(left, right):
            if left == right:
                return nums[left]
        
            # Corrected logic: subtract the opponent's score
            choose_left = nums[left] - dp(left + 1, right)
            choose_right = nums[right] - dp(left, right - 1)
            
            # The player chooses the option that maximizes their score
            return max(choose_left, choose_right)

        # Check if the first player's score is non-negative
        return dp(0, len(nums) - 1) >= 0
        
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        
        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])
        
        return dp[0][n - 1] >= 0


        # @cache
        # def dp(left, right):
        #     if right - left == 1:
        #        return max(nums[left], nums[right])    
        #     if left > right:
        #         return 0        
        #     if left == right:
        #         return nums[left]
        
        #     choose_left = nums[left] + min(dp(left + 1, right - 1), dp(left + 2, right))
        #     choose_right = nums[right] + min(dp(left, right - 2), dp(left + 1, right - 1))
        #     return max(choose_left, choose_right)
        
        # n = len(nums)
        # alice = dp(0, n-1)
        # # print(alice)
        # return alice >= sum(nums)//2
        
       