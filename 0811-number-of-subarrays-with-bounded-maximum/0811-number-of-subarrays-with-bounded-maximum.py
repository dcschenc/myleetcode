class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0795.Number%20of%20Subarrays%20with%20Bounded%20Maximum
        def f(x):
            cnt = t = 0
            for v in nums:
                t = 0 if v > x else t + 1
                cnt += t
            return cnt

        return f(right) - f(left - 1)
