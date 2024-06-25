class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        # Calculate the length of the input list of numbers
        size = len(nums)
      
        # If there is only one number, return it as a string
        if size == 1:
            return str(nums[0])
      
        # If there are two numbers, return them as a division
        if size == 2:
            return f'{nums[0]}/{nums[1]}'
      
        # For more than two numbers, the optimal division is to divide the first number
        # by the result of the division of all remaining numbers to achieve the largest result.
        # This is done by grouping all but the first number inside parentheses.
        return f'{nums[0]}/(' + "/".join(map(str, nums[1:])) + ')'
