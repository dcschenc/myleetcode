class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        idx = 0
        for i in range(1, n-k+1):
            if nums[i] > nums[idx]:
                idx = i
        return nums[idx:idx+k]
