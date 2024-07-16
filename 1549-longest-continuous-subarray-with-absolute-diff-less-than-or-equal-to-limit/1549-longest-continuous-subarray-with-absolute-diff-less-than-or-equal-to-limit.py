from sortedcontainers import SortedList
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_length = 0

        for right in range(len(nums)):
            # Maintain max_deque in decreasing order
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain min_deque in increasing order
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # If the difference between max and min in the current window exceeds the limit, shrink the window
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove the elements that are out of the new window's range
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)
        
        return max_length

        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1438.Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit
        sl = SortedList()
        ans = j = 0
        for i, v in enumerate(nums):
            sl.add(v)
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[j])
                j += 1
            ans = max(ans, i - j + 1)
        return ans