class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0456.132%20Pattern
        n = len(nums)
        if n < 3: return False

        # Initialize the stack to store elements in decreasing order.
        stack = []
        third = float('-inf')  
        # Iterate the array from right to left.
        for i in range(n - 1, -1, -1):
            if nums[i] < third:  return True
            # update the third element with the top of the stack and pop the stack.
            while stack and nums[i] > stack[-1]:
                third = stack.pop()

            # Push the current element onto the stack.
            stack.append(nums[i])

        return False  # No valid subsequence was found.

