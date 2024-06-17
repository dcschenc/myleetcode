class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i, val in enumerate(nums):
            if target - val in hmap:
                return [hmap[target-val], i]
            else:
                hmap[val] = i
        
        