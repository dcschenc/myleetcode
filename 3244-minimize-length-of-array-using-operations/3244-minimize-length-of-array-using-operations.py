class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3012.Minimize%20Length%20of%20Array%20Using%20Operations
        mi = min(nums)
        if any(x % mi for x in nums):
            return 1
        return (nums.count(mi) + 1) // 2

