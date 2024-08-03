class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        m, n = len(operations), len(nums)
        hm = {num : i for i, num in enumerate(nums)}
        for num, val in operations:
            idx = hm[num]
            nums[idx] = val
            hm[val] = idx
        return nums