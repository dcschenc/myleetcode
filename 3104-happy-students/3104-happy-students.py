class Solution:
    def countWays(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2860.Happy%20Students
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n + 1):
            if i and nums[i - 1] >= i:
                continue
            if i < n and nums[i] <= i:
                continue
            ans += 1
        return ans

        nums.sort()
        size = 0
        i, n = 0, len(nums)
        ans = 0
        for i in range(n):
            if i == 0 and nums[i] > size:
                ans += 1
            size += 1
            if i == n - 1 and nums[i] < size or nums[i] < size and nums[i + 1] > size:
                ans += 1
        return ans
