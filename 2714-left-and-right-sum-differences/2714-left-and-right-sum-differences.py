class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # https://leetcode.com/problems/left-and-right-sum-differences/
        ans = [0]
        n = len(nums)
        for i in range(1, n):
            ans.append(ans[-1] + nums[i - 1])

        cur = 0
        for i in range(n - 1, -1, -1):
            ans[i] = abs(ans[i] - cur)
            cur += nums[i]
        return ans
