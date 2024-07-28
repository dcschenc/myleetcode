class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2008.Maximum%20Earnings%20From%20Taxi
        # Define a memoized recursive function to compute maximum earnings
        @lru_cache(None)  # Decorator to cache the results of the function calls
        def dfs(i: int) -> int:
            # Base case: when all rides have been processed
            if i >= len(rides):
                return 0
              
            # Extract the start, end and tip for the current ride
            start, end, tip = rides[i]
          
            # Find the next ride that can be taken after the current ride ends
            j = bisect_left(rides, end, lo=i + 1, key=lambda x: x[0])
          
            # Decision:
            # 1. Skip the current ride and move to the next one: dfs(index + 1)
            # 2. Take the current ride and then move to the next possible ride: dfs(next_index) + (end - start + tip)
            # Choose the option that yields the maximum earnings
            return max(dfs(i + 1), dfs(j) + end - start + tip)
      
        # Sort the rides by start time to enable binary search
        rides.sort()
      
        # Start the dfs from the first ride
        return dfs(0)
