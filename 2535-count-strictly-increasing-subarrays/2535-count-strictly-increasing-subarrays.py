class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        prectn = [1] * n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                prectn[i] += prectn[i-1]
        return sum(prectn)