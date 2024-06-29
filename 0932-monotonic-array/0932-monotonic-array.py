class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        incr,decr = 0, 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                incr += 1
            if nums[i] < nums[i-1]:
                decr += 1
            if incr != 0 and decr != 0:
                return False
        return True