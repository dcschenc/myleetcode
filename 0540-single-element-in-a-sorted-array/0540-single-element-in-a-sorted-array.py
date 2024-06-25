class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if (mid % 2 == 0 and nums[mid] != nums[mid + 1]) \
                or (mid % 2 == 1 and nums[mid] != nums[mid - 1]):
            # if nums[mid] != nums[mid ^ 1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

        # left, right = 0, len(nums) - 1
        # while left < right:
        #     mid = left + (right - left) // 2
        #     # Ensure mid is an even index
        #     if mid % 2 == 1:
        #         mid -= 1
        #     # Check if the unique element is on the left or right side
        #     if nums[mid] == nums[mid + 1]:
        #         left = mid + 2
        #     else:
        #         right = mid

        # return nums[left]
        
        # n = len(nums)
        # left, right = 0, n-1
        # while left < right:            
        #     mid = (left + right)//2
        #     if mid > 0 and nums[mid-1] != nums[mid] and nums[mid+1] != nums[mid]:
        #         return nums[mid]
        #     if mid==0 and nums[mid] != nums[mid+1]:
        #         return nums[mid]
        #     elif mid == n-1 and nums[mid] != nums[mid-1]:
        #         return nums[mid]
        #     else:
        #         if nums[mid] == nums[mid-1]:
        #             if (mid-left)%2 == 0:
        #                 right = mid
        #             else:
        #                 left = mid+1
        #         if nums[mid] == nums[mid+1]:
        #             if (mid-left)%2 == 0:
        #                 left = mid
        #             else:
        #                 right = mid-1
        # return nums[left]
                    
             
