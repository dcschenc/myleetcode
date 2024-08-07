class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2560.House%20Robber%20IV
        def can_rob(capacity):
            count = 0
            prev_idx = None
            for idx, num in enumerate(nums):
                if num > capacity:
                    continue
                if idx - 1 == prev_idx:
                    continue
                prev_idx = idx
                count += 1
                if count == k:
                    return True
            return False
        
        left, right = min(nums), max(nums)         
        while left <= right:
            mid = (left + right) // 2      
            ### can rob k and more, then decrease capacity ###      
            if can_rob(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left