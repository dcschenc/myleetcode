class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans, i = [], 0
        while i < n:
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i+3])
            i += 3
        return ans