class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1887.Reduction%20Operations%20to%20Make%20the%20Array%20Elements%20Equal
        nums.sort()
        ans = cnt = 0
        for i, v in enumerate(nums[1:]):
            if v != nums[i]:
                cnt += 1
            ans += cnt
        return ans