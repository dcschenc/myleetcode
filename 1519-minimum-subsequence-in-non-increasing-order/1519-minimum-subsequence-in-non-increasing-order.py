class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse= True)
        total = sum(nums)
        sub_total = 0
        for i in range(len(nums)):
            sub_total += nums[i]
            if sub_total > total - sub_total:
                break
        return nums[:i+1]