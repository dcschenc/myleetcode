class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # https://leetcode.com/problems/bitwise-and-of-numbers-range/editorial/
        shift = 0   
        # find the common 1-bits
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        return right << shift

        # As a result, we then can reformulate the problem as "given two integer numbers, we are asked to find the common prefix of their binary strings."
        # Loop until 'left' is not less than 'right'
        while left < right:
            # We use the trick "right &= right - 1" to clear the least significant bit of 'right'
            # This effectively reduces 'right' each time, moving towards 'left'
            right &= right - 1
      
        # At the point where the while loop stops, 'left' and 'right' have the same prefix for 
        # their binary representations which is the answer to the problem.
        return right