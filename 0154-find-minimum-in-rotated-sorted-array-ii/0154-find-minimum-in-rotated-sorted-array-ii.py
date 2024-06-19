class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]
    
#         while len(nums) > 1:
#             if nums[0] == nums[-1]:
#                 nums.pop()
#             else:
#                 break
#         if len(nums) == 1:
#             return nums[0]
#         left, right = 0, len(nums)-1
        
#         while left <= right:
#             mid = (left+right)//2                        
#             if nums[mid] > nums[mid+1] and nums[mid] >= nums[mid-1]:
#                 return nums[mid+1]
#             elif nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
#                 return nums[mid]
#             elif nums[mid] > nums[-1]:
#                 left = mid+1
#             else:
#                 right = mid-1
#             # if mid == 0 or mid == len(nums)-1:
#                 # return nums[mid]
            
#         return nums[0]