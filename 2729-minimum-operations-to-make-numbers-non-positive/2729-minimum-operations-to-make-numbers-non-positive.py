class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2702.Minimum%20Operations%20to%20Make%20Numbers%20Non-positive
        def check(t: int) -> bool:
            cnt = 0
            for v in nums:
                if v > t * y:
                    cnt += ceil((v - t * y) / (x - y))
            return cnt <= t

        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l