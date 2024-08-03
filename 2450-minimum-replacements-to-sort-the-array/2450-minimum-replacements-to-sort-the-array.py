class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2366.Minimum%20Replacements%20to%20Sort%20the%20Array
        ans = 0
        n = len(nums)
        mx = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= mx:
                mx = nums[i]
                continue
            k = (nums[i] + mx - 1) // mx
            ans += k - 1
            mx = nums[i] // k
        return ans
