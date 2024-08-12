from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        # Create a SortedList to store the current window of numbers
        sorted_list = SortedList()
        # Initialize the answer with infinity, representing a large number
        min_diff = float('inf')

        # Start iterating from the target index to the end of the list
        for i in range(x, len(nums)):
            # Add the (current index - target)th element to maintain the window
            sorted_list.add(nums[i - x])
            # Find the index in the sorted list where nums[i] would fit
            insert_pos = bisect_left(sorted_list, nums[i])
          
            # If there is an element on the right, update min_diff
            if insert_pos < len(sorted_list):
                min_diff = min(min_diff, sorted_list[insert_pos] - nums[i])
            # If there is an element on the left, update min_diff
            if insert_pos > 0:
                min_diff = min(min_diff, nums[i] - sorted_list[insert_pos - 1])

        # Return the minimum absolute difference found
        return min_diff

        