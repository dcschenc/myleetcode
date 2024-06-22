class Solution:
    def findNthDigit(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0400.Nth%20Digit
        
        # initialize variables
        # 'digit_length' represents the current digit length we are calculating (e.g., 1 for 0-9, 2 for 10-99, etc.)
        digit_length = 1
      
        # 'digit_count' represents the count of numbers that can be formed with the current 'digit_length'
        digit_count = 9

        # loop to find the correct digit length for the given 'n'
        while digit_length * digit_count < n:
            # subtract the total length covered so far
            n -= digit_length * digit_count

            # increment the digit length since we move on to numbers with more digits
            digit_length += 1

            # increase digit_count by a factor of 10 as we move to the next set of numbers
            digit_count *= 10

        # find the actual number where the result digit is located
        number = 10 ** (digit_length - 1) + (n - 1) // digit_length

        # find the index of the digit within 'number'
        index_within_number = (n - 1) % digit_length

        # get the digit at the calculated index of the number and return it
        return int(str(number)[index_within_number])
