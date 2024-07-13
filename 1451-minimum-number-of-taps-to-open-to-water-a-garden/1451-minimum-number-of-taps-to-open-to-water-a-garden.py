class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        # Define an infinite value
        INF = int(1e9)
        
        # Create a list to store the minimum number of taps needed for each position
        dp = [INF] * (n + 1)
        
        # Initialize the starting position of the garden
        dp[0] = 0
        
        for i in range(n + 1):
            # Calculate the leftmost position reachable by the current tap
            tap_start = max(0, i - ranges[i])
            # Calculate the rightmost position reachable by the current tap
            tap_end = min(n, i + ranges[i])
            
            for j in range(tap_start, tap_end + 1):
                # Update with the minimum number of taps
                dp[tap_end] = min(dp[tap_end], dp[j] + 1)
        
        # Check if the garden can be watered completely
        if dp[n] == INF:
            # Garden cannot be watered
            return -1
        
        # Return the minimum number of taps needed to water the entire garden
        return dp[n]

        
        # # Initialize an array to track the furthest right position that can be covered by opening a tap from each point
        # max_right_from_left = [0] * (n + 1)
      
        # # Iterate over the taps and calculate the range each tap can cover. Then update the `max_right_from_left` array.
        # for tap_index, tap_range in enumerate(ranges):
        #     left_bound = max(0, tap_index - tap_range)
        #     right_bound = tap_index + tap_range
        #     max_right_from_left[left_bound] = max(max_right_from_left[left_bound], right_bound) 

        # # Initialize variables for tracking the answer, the maximum distance covered so far, and the previous maximum before the last tap.
        # taps_required = 0
        # max_covered_so_far = 0
        # previous_max = 0

        # # Iterate through the garden and update the max coverage.
        # for pos in range(n):
        #     max_covered_so_far = max(max_covered_so_far, max_right_from_left[pos])
          
        #     # If at any position, the max covered distance is less than or equal to the current position, the garden cannot be fully watered.
        #     if max_covered_so_far <= pos:
        #         return -1
          
        #     # If the current position reaches the previous maximum coverage, it's time to open a new tap
        #     if previous_max == pos:
        #         taps_required += 1
        #         previous_max = max_covered_so_far

        # # Return the minimum number of taps required to water the entire garden.
        # return taps_required

        # intervals = []
        # for i in range(n):
        #     intervals.append((i - ranges[i], i + ranges[i]))
        # intervals.sort(key=lambda x:(x[0], -x[1]))
        # cur, l, cnt = 0, 0, 0
        # while l < n:
        #     j = l
        #     right = -1
        #     while j < n and intervals[j][0] <= cur:
        #         right = max(right, intervals[j][1])
        #         j += 1
        #     if right != -1:
        #         cur = right
        #         cnt += 1
        #     else:
        #         return -1
        #     if cur == n:
        #         return cnt
        #     l = j
        # return cnt
        
        