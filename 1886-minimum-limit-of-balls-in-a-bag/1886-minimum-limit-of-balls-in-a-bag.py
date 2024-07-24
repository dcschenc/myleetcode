class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1760.Minimum%20Limit%20of%20Balls%20in%20a%20Bag
        def can_split(x):
            cnt = 0
            for num in nums:
                cnt += math.ceil(num/x) - 1
            return cnt <= maxOperations
        
        lo, hi = 1, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_split(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo