class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2563.Count%20the%20Number%20of%20Fair%20Pairs
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            left = bisect_left(nums, lower - nums[i], i + 1)
            right = bisect_right(nums, upper - nums[i], i + 1) 
            if left == right:
                continue
            ans += right - left
        return ans