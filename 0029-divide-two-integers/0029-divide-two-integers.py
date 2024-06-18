class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Define the boundaries for an integer (32-bit signed integer)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31      

        # Determine the sign of the output. If dividend and divisor have different signs, result will be negative
        sign = -1 if (dividend * divisor) < 0 else 1      

        # Work with positive values for both dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)      
        
        # Initialize the total quotient
        total_quotient = 0      
        # Loop to find how many times the divisor can fit into the dividend
        while dividend >= divisor:
            # Count will keep track of the number of times we can double the divisor while still being less than or equal to dividend
            count = 0
            # Double the divisor as much as possible without exceeding the dividend
            while dividend >= (divisor << (count + 1)):
                count += 1
            # Increment total_quotient by the number of times we doubled the divisor
            total_quotient += 1 << count
            # Decrease dividend by the matched part which we just calculated
            dividend -= divisor << count
      
        # Multiply the result by the sign
        result = sign * total_quotient
      
        # Check and correct for overflow: if result is out of the 32-bit signed integer range, clamp it to INT_MAX
        if result < INT_MIN:
            return INT_MIN
        elif result > INT_MAX:
            return INT_MAX
        else:
            return result
            