from collections import deque
class Solution:
    def thirdMax(self, nums: List[int]) -> int:   
        if len(nums) == 2:
            return max(nums)
        tops = []       
        for val in nums:
            if val in tops:
                continue
            if len(tops) < 3:
                tops.append(val)
                tops.sort()
                continue
            if val > tops[2]:               
                tops[0] = tops[1]
                tops[1] = tops[2]
                tops[2] = val
            elif val > tops[1]:
                tops[0] = tops[1]
                tops[1] = val
            elif val > tops[0]:
                tops[0] = val
        if len(tops) < 3:
            return tops[-1]
        return tops[0]
            
        