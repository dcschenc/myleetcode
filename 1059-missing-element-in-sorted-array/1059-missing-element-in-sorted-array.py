class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/blob/main/solution/1000-1099/1060.Missing%20Element%20in%20Sorted%20Array/README.md
        def missing_count(idx):
            # Calculate how many numbers are missing until index idx
            return nums[idx] - nums[0] - idx
        
        n = len(nums)
        
        # If the K-th missing number is beyond the last element in the array
        if missing_count(n - 1) < k:
            return nums[-1] + (k - missing_count(n - 1))
        
        # Binary search to find the correct index
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if missing_count(mid) < k:
                left = mid + 1
            else:
                right = mid
        
        # The K-th missing number is between nums[left - 1] and nums[left]
        return nums[left - 1] + (k - missing_count(left - 1))
