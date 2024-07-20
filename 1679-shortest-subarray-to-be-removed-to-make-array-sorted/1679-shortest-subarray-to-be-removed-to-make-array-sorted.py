class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1574.Shortest%20Subarray%20to%20be%20Removed%20to%20Make%20Array%20Sorted
        n = len(arr)
        i, j = 0, n - 1
        while i + 1 < n and arr[i] <= arr[i + 1]:
            i += 1
        while j - 1 >= 0 and arr[j - 1] <= arr[j]:
            j -= 1
        if i >= j:
            return 0
        ans = min(n - i - 1, j)
        for l in range(i + 1):
            r = bisect_left(arr, arr[l], lo=j)
            ans = min(ans, r - l - 1)
        return ans


        # Length of the array
        length = len(arr)
      
        # Initialize two pointers for the beginning and end of the array
        left = 0
        right = length - 1
      
        # Move the left pointer to the right as long as the subarray is non-decreasing
        while left + 1 < length and arr[left] <= arr[left + 1]:
            left += 1
      
        # Move the right pointer to the left as long as the subarray is non-decreasing
        while right - 1 >= 0 and arr[right - 1] <= arr[right]:
            right -= 1
      
        # If the whole array is already non-decreasing, return 0
        if left >= right:
            return 0
      
        # Calculate the length of the remaining array to be removed
        min_length_to_remove = min(length - left - 1, right)
      
        # Reinitialize the right pointer for the next loop
        new_right = right
      
        # Check for the shortest subarray from the left side to the midpoint
        for new_left in range(left + 1):
            # Increment the right pointer until the elements on both sides are non-decreasing
            while new_right < length and arr[new_right] < arr[new_left]:
                new_right += 1
            # Update the minimum length if a shorter subarray is found
            min_length_to_remove = min(min_length_to_remove, new_right - new_left - 1)

        # Return the minimum length of the subarray to remove to make array non-decreasing
        return min_length_to_remove
        
  