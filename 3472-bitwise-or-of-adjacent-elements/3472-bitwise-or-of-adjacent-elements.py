class Solution:
    def orArray(self, nums: List[int]) -> List[int]:
        i, n = 0, len(nums)
        ans = []
        while i < n - 1:
            ans.append(nums[i] | nums[i + 1])
            i += 1
        return ans