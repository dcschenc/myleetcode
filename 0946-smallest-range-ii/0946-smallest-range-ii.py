class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0910.Smallest%20Range%20II
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        nums.sort()
        n = len(nums)
        # Initial result with the difference between max and min
        result = nums[-1] - nums[0]  

        for i in range(n):
            mi = min(nums[0] + k, nums[i] - k)
            mx = max(nums[i - 1] + k, nums[-1] - k)
            result = min(result, mx - mi)

        return result