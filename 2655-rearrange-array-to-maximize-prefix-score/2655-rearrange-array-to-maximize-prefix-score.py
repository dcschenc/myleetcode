class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2587.Rearrange%20Array%20to%20Maximize%20Prefix%20Score
        nums.sort(reverse=True)
        s = 0
        for i, x in enumerate(nums):
            s += x
            if s <= 0:
                return i
        return len(nums)

        # nums.sort(reverse=True)
        # ans = 0
        # cur = 0
        # for i in range(len(nums)):
        #     cur += nums[i]
        #     if cur > 0:
        #         ans += 1
        #     else:
        #         return ans
        # return ans
        