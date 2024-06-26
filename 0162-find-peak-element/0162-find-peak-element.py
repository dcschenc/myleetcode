class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
        
        # left, right = 0, len(nums)-1
        # while left < right:
        #     mid = left + (right-left)//2
        #     if mid == 0 and nums[mid] > nums[mid+1]:
        #         return mid
        #     elif mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
        #         return mid
        #     elif nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        #         return mid
        #     elif nums[mid] < nums[mid+1]:
        #         left = mid + 1
        #     else:
        #         right = mid-1
        # return left