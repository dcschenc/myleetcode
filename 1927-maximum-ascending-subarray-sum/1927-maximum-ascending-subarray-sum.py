class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1800.Maximum%20Ascending%20Subarray%20Sum
        ans = t = 0
        for i, v in enumerate(nums):
            if i == 0 or v > nums[i - 1]:
                t += v
                ans = max(ans, t)
            else:
                t = v
        return ans
        
        # presum = nums[:]
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         presum[i] += presum[i-1]
        # return max(presum)