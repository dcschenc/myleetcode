class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        s = set()
        for i in range(n-1):
            if nums[i] + nums[i + 1] in s:
                return True
            s.add(nums[i] + nums[i + 1])
        return False