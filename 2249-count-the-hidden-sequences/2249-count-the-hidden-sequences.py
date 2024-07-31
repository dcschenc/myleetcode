class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = max_val = 0
        current_sum = 0
        
        for diff in differences:
            current_sum += diff
            min_val = min(min_val, current_sum)
            max_val = max(max_val, current_sum)
        
        valid_start_range_lower = lower - min_val
        valid_start_range_upper = upper - max_val
        
        if valid_start_range_lower > valid_start_range_upper:
            return 0
        
        return valid_start_range_upper - valid_start_range_lower + 1

        # Initialize the variables: current_sum to track the running sum,
        # min_value to keep the minimum value encountered, and max_value
        # for the maximum value encountered.
        current_sum = min_value = max_value = 0
      
        # Iterate through each difference in the array
        for diff in differences:
            # Add the current difference to the running sum
            current_sum += diff
            # Update the minimum value if the new current_sum is lower
            min_value = min(min_value, current_sum)
            # Update the maximum value if the new current_sum is higher
            max_value = max(max_value, current_sum)
      
        # Calculate the width of the range spanned by the differences
        range_width = max_value - min_value
        # Calculate the total number of distinct arrays that can be formed
        # within the given upper and lower bounds. Here we also include the
        # '+ 1' offset to account for inclusive bounds.
        # If the resulting number is negative, we use max(0, ...) to default to 0.
        # This represents cases where no valid arrays can be formulated.
        num_of_arrays = max(0, (upper - lower) - range_width + 1)
      
        return num_of_arrays
