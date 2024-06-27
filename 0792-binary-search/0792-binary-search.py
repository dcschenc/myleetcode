class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right =0, len(nums) - 1
        # mid = len(nums)//2
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                # mid = left + (right-left)//2
            else:
                right = mid - 1
                # mid = left + (right-left)//2
        # if nums[left] == target:
        #     return left
        return -1