class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
    
        # if len(nums) == 1:
        #     return nums[0]
        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = left + (right-left)//2
        #     if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        #         return nums[mid+1]
        #     elif nums[mid] > nums[-1]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return nums[0]