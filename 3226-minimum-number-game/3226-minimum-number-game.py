class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        n = len(nums)
        for i in range(0, n-1, 2):
            ans.append(nums[i+1])
            ans.append(nums[i])
        return ans