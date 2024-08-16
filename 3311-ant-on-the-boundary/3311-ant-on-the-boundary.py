class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3028.Ant%20on%20the%20Boundary
        cur, ans = 0, 0
        for num in nums:
            cur += num
            if cur == 0:
                ans += 1
        return ans