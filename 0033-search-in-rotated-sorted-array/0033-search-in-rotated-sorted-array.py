class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

        # if len(nums) == 1:
        #     return 0 if nums[0] == target else -1
        
        # left, right = 0, len(nums)-1
        # # right_val = nums[-1]
        # while left <= right:
        #     mid = left + (right-left)//2
        #     if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
        #         break
        #     if nums[mid] > nums[-1]:
        #         left = mid + 1
        #     else:
        #         right = mid -1 
        
        # # print(mid)
        # left, right = 0, mid
        # if target >= nums[left] and target <= nums[right]:
        #     pass
        # else:
        #     left = mid + 1
        #     right = len(nums) - 1
        
        # #### binary search for value ####
        # while left <= right:
        #     mid = left + (right-left)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        # return -1