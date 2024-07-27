class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        max_val = 100  # Given constraint: 1 <= nums[i] <= 100
        n = len(nums)
        
        # Prefix sum array for frequencies of each number from 1 to 100
        prefix = [[0] * (max_val + 1) for _ in range(n + 1)]
        
        # Build the prefix sum array
        for i in range(n):
            for j in range(1, max_val + 1):
                prefix[i + 1][j] = prefix[i][j]
            prefix[i + 1][nums[i]] += 1
        
        result = []
        
        for l, r in queries:
            # Find all unique numbers in the subarray nums[l..r]
            freq = [prefix[r + 1][i] - prefix[l][i] for i in range(1, max_val + 1)]
            unique_nums = [i for i in range(1, max_val + 1) if freq[i - 1] > 0]
            
            # Calculate the minimum absolute difference between consecutive unique numbers
            min_diff = float('inf')
            for i in range(1, len(unique_nums)):
                min_diff = min(min_diff, unique_nums[i] - unique_nums[i - 1])
            
            # If no valid pair is found, return -1
            if min_diff == float('inf'):
                result.append(-1)
            else:
                result.append(min_diff)
        
        return result
        
        # Get the lengths of the input list and the queries
        num_count = len(nums)
        query_count = len(queries)
      
        # Initialize a prefix sum array with zeros
        # This array will store the counts of each number from 1 to 100 up to index i
        prefix_sum = [[0] * 101 for _ in range(num_count + 1)]
      
        # Calculate prefix sums
        for i in range(1, num_count + 1):
            for j in range(1, 101):
                # Check if the current num is equal to the current value j
                if nums[i - 1] == j:
                    count_increment = 1  
                else:
                    count_increment = 0
                prefix_sum[i][j] = prefix_sum[i - 1][j] + count_increment

        # Prepare a list to store the answers to each query
        results = []
      
        # Process each query
        for i in range(query_count):
            # Define the range for the current query
            left, right = queries[i][0], queries[i][1] + 1
          
            # Initialize the minimum difference to positive infinity
            min_diff = inf
            # Initialize the last seen number variable
            last_seen = -1
          
            # Loop through the range of possible values 1 to 100
            for j in range(1, 101):
                # If the number j is present in the current segment (between left and right)
                if prefix_sum[right][j] - prefix_sum[left][j] > 0:
                    # If this is not the first number we've seen, update the min_diff
                    if last_seen != -1:
                        min_diff = min(min_diff, j - last_seen)
                    # Update last_seen with the current number
                    last_seen = j
          
            # If min_diff is still infinity, it means no numbers are present, so set the result to -1
            if min_diff == inf:
                min_diff = -1
          
            # Append the result of the current query to the results list
            results.append(min_diff)
          
        # Return the list of results
        return results