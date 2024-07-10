class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1191.K-Concatenation%20Maximum%20Sum
        
        # Initialize variables
        total_sum = max_prefix = min_prefix = max_subarray_sum = 0
      
        # Calculate max subarray sum for a single array iteration
        for num in arr:
            total_sum += num
            max_prefix = max(max_prefix, total_sum)
            min_prefix = min(min_prefix, total_sum)
            max_subarray_sum = max(max_subarray_sum, total_sum - min_prefix)
      
        # The result after a single iteration
        result = max_subarray_sum
        mod = 10**9 + 7
      
        # If k is 1, return the result of a single array's max subarray sum
        if k == 1:
            return result % mod
      
        # Calculate the maximum suffix sum for potential use in concatenated arrays
        max_suffix = total_sum - min_prefix
      
        # Update result for potential double array combination
        result = max(result, max_prefix + max_suffix)
      
        # If the array sum is positive, calculate the max sum when array is concatenated k times
        if total_sum > 0:
            result = max(result, ((k - 2) * total_sum) + max_prefix + max_suffix)
      
        return result % mod  # Return the result modulo the provided modulus