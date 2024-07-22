class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1671.Minimum%20Number%20of%20Removals%20to%20Make%20Mountain%20Array
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        return n - max(a + b - 1 for a, b in zip(left, right) if a > 1 and b > 1)