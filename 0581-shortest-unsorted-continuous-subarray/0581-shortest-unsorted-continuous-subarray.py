class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Find the leftmost index where the array is out of order
        left, right = 0, n - 1
        while left < n - 1 and nums[left] <= nums[left + 1]:
            left += 1

        # If the array is already sorted
        if left == n - 1:
            return 0

        # Find the rightmost index where the array is out of order
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1

        # Find the minimum and maximum values within the unsorted subarray
        min_val, max_val = min(nums[left:right+1]), max(nums[left:right+1])

        # Extend the unsorted subarray to include any elements greater than min_val
        while left >= 0 and nums[left] > min_val:
            left -= 1

        # Extend the unsorted subarray to include any elements smaller than max_val
        while right < n and nums[right] < max_val:
            right += 1

        # Calculate the length of the unsorted subarray
        length = right - left - 1

        return length



        stack = []
        left, right = len(nums), 0

        # Find the leftmost index where the array is out of order
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                left = min(left, stack.pop())
            stack.append(i)

        stack = []

        # Find the rightmost index where the array is out of order
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                right = max(right, stack.pop())
            stack.append(i)

        # Calculate the length of the unsorted subarray
        length = right - left + 1 if right > left else 0

        return length