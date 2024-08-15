class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        # for x, y in itertools.combinations(nums, 2):
        #     if (x | y) & 1 == 0:
        #         return True
        # return False
        
        # Initialize a counter for the number of elements with trailing zeros
        trailing_zero_count = 0
      
        # Iterate over each number in the list
        for number in nums:
            # Check if the last bit is 0 (which means the number is even)
            if (number & 1) == 0:
                # Increment the counter for numbers with trailing zero
                trailing_zero_count += 1
              
            # If we already have at least two numbers with trailing zeros, return True
            if trailing_zero_count >= 2:
                return True
      
        # If the function hasn't returned yet, it means we have less than 2 numbers with trailing zeros
        return False
