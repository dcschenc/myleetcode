class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0611.Valid%20Triangle%20Number
        nums.sort()
        ans, n = 0, len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
                ans += k - j
        return ans
        