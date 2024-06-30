class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # Initialize a stack to keep track of indices of the potential start of the ramp.
        stack = []
      
        # Iterate through the given numbers along with their indices.
        for index, value in enumerate(nums):
            # If the stack is empty or the current value is less than the value at the last index of the stack,
            # this could be a potential start of a ramp, so store the index.
            if not stack or nums[stack[-1]] > value:
                stack.append(index)
              
        # Initialize the answer variable with 0 to keep track of the maximum width.
        max_width = 0
      
        # Iterate backwards from the end of nums to find the maximum ramp.
        # We go backwards since we're looking for the largest index j (end of the ramp)
        # that forms a ramp with the start indices in the stack.
        for i in range(len(nums) - 1, -1, -1):
            # While the stack is not empty and the current number is greater than or equal to
            # the number at the index of the top of the stack, we have a potential ramp.
            while stack and nums[stack[-1]] <= nums[i]:
                # Calculate the width of the ramp and update the max_width if this ramp is wider.
                max_width = max(max_width, i - stack.pop())
            # If the stack becomes empty, no more start positions are left to check,
            # and the maximum ramp is found.
            if not stack:
                break
              
        # Return the maximum width of the ramp found.
        return max_width