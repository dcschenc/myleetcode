class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1 
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[right]: # Fail to estimate which side is sorted
                right -= 1  # In worst case: O(n)
            elif nums[left] <= nums[mid]: # Left side of mid is sorted
                if  nums[left] <= target < nums[mid]: # Target in the left side
                    right = mid - 1
                else: # in right side
                    left = mid + 1
            else: # Right side is sorted
                if  nums[mid] < target <= nums[right]: # Target in the right side
                    left = mid + 1
                else: # in left side
                    right = mid - 1
        return False