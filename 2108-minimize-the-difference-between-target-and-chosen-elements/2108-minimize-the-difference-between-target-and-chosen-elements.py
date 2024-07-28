class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Initialize a set containing just the element 0
        # This set will hold all possible sums up till the current row
        possible_sums = {0}

        # Iterate over each row in the matrix
        for row in mat:
            # Use a set comprehension to generate all possible sums
            # by adding each element in the current row to all possible sums calculated in the previous step
            # This ensures we only consider sums that include exactly one element from each row
            possible_sums = {elem + row_elem for elem in possible_sums for row_elem in row}
      
        # Find the minimum absolute difference between any possible sum and the target
        # This is done by iterating over all possible sums and computing the absolute difference with the target
        min_difference = min(abs(sum_val - target) for sum_val in possible_sums)

        # Return the minimum difference found
        return min_difference