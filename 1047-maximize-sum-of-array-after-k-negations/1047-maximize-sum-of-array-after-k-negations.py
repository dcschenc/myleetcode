class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        while i < len(nums) and k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            i += 1
            k -= 1
        if k > 0:
            if k % 2 == 1:
                if i == len(nums):
                    nums[i-1] = -nums[i-1]
                elif nums[i] < nums[i-1]:
                    nums[i] = -nums[i]
                else:
                    nums[i-1] = -nums[i-1]
        
        return sum(nums)