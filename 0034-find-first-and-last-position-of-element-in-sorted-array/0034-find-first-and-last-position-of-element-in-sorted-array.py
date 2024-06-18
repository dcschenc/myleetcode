class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        l, r = -1, -1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                l = mid
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if l == -1:
            return [-1, -1]
        r = l
        while r < len(nums)-1:
           
            if nums[r+1] == target:
                 r+=1
            else:
                break
            
        return [l, r]

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target and (mid == (len(nums) - 1) or nums[mid+1] != target):
                r = mid
                break
            elif nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return [l, r]