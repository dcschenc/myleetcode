class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        left, right = start, start
        n = len(nums)
        mi = inf
        while left >= 0:
            if nums[left] == target:
                mi = start - left
                break
            left -= 1

        while right < n:
            if nums[right] == target:
                mi = min(mi, right - start)
                break
            right += 1
        
        return mi 
        