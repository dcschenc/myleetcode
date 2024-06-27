class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        mx = -1
        for i in range(2, n):            
            if (mx := max(mx, nums[i-2])) > nums[i]:
                return False            
        return True