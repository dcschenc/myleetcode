class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-value-of-the-partition/
        nums.sort()
        return min(b - a for a, b in pairwise(nums))
            
        ans = float('inf')
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            ans = min(ans, nums[i] - nums[i-1])
        return ans