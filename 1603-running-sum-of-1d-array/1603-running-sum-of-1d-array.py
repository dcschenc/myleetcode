from itertools import accumulate
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))

        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums