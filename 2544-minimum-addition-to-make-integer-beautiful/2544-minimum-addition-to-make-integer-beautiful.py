class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:        
        # https://algo.monster/liteproblems/2457
        
        # Function to compute the sum of digits of an integer 'x'.
        def sum_of_digits(x: int) -> int:
            total_sum = 0
            while x > 0:
                total_sum += x % 10
                x //= 10
            return total_sum

        increments = 0  # Variable to keep track of how much we need to add to 'n' to make it beautiful.

        # Loop until the sum of digits of 'n + increments' is greater than 'target'.
        while sum_of_digits(n + increments) > target:
            temp_number = n + increments
            power_of_ten = 10
            # Find trailing zeros by reducing 'temp_number' until it's not divisible by 10.
            while temp_number % 10 == 0:
                temp_number //= 10
                power_of_ten *= 10  # Increase power of 10 correspondingly.

            # Compute increments such that 'n + increments' eliminates trailing zeros,
            # and reduces digit sum. Calculate the next temp number and adjust increments.
            increments = (temp_number // 10 + 1) * power_of_ten - n
          
        # Return the total amount required to add to 'n' to make it beautiful.
        return increments