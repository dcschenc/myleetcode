class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i, can_square):
            if i >= n:
                return 0

            max_val = 0

            if can_square:
                max_val = max(max_val, nums[i] * nums[i], nums[i] * nums[i] + dfs(i + 1, False))
            
            max_val = max(max_val, nums[i], nums[i] + dfs(i + 1, can_square))

            return max_val

        n = len(nums)

        return max([dfs(i, True) for i in range(n)]) 

        
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        cur = 0
        for i in range(n):
            prefix[i] = cur
            cur = cur + nums[i]
            if cur < 0:
                cur = 0
        cur = 0
        for i in range(n-1, -1, -1):
            postfix[i] = cur
            cur += nums[i]
            if cur < 0:
                cur = 0
        ans = 0
        for i in range(n):
            ans = max(ans, nums[i] * nums[i] + prefix[i] + postfix[i])
        return ans

        