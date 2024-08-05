class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2464.Minimum%20Subarrays%20in%20a%20Valid%20Split
        @cache
        def dp(i):
            if i >= n:
                return 0
            ans = float('inf')
            for j in range(i, n):
                if gcd(nums[i], nums[j]) > 1:
                    ans = min(ans, 1 + dp(j + 1))
            return ans
                
        n = len(nums)
        ans = dp(0)        
        dp.cache_clear()
        return ans if ans != float('inf') else -1

      