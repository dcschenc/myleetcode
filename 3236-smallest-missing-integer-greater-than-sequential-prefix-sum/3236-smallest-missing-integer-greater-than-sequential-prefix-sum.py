class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2996.Smallest%20Missing%20Integer%20Greater%20Than%20Sequential%20Prefix%20Sum
        s, i = nums[0], 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            s += nums[i]
            i += 1
        ss = set(nums)
        for x in count(s):
            if x not in ss:
                return x
