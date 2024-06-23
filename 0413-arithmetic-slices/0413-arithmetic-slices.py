class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:  
        n = len(nums)
        if n < 3: return 0
        left, total = 0, 0
        for right in range(2, n):
            if nums[right] - nums[right - 1] == nums[right - 1] - nums[right - 2]:
                # total += (right - left) + 1 if right - left >= 2 else 1
                if right - left == 2:
                    total += 1
                else:
                    total += (right - left - 1)
            else:
                left = right - 1
        return total

        # if len(nums) < 3:
        #     return 0
            
        # count = 0
        # current = 0

        # for i in range(2, len(nums)):
        #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        #         current += 1
        #         count += current
        #     else:
        #         current = 0

        # return count