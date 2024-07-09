class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        left = bisect_left(nums, target)
        right = bisect_right(nums, target)
        return right - left > len(nums) // 2
        
        # left, right = 0, len(nums) - 1        
        # while left < right:
        #     mid = (left + right)//2
        #     if nums[mid] < target:
        #         left = mid + 1
        #     else:
        #         right = mid
        
        # n = len(nums)
        # return left + n // 2 < n and nums[left + n // 2] == target

        # if left + len(nums)//2 < len(nums) and nums[left + len(nums)//2] == target:
        #     return True
        # return False      


        # cnt = 0
        # for num in nums:
        #     if target == num:
        #         cnt += 1
        # return cnt > len(nums)/2