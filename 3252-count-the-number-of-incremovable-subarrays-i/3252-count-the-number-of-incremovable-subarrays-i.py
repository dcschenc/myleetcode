class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:        
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2970.Count%20the%20Number%20of%20Incremovable%20Subarrays%20I
        i, n = 0, len(nums)
        while i + 1 < n and nums[i] < nums[i + 1]:
            i += 1
        if i == n - 1:
            return n * (n + 1) // 2
        ans = i + 2
        j = n - 1
        while j:
            while i >= 0 and nums[i] >= nums[j]:
                i -= 1
            ans += i + 2
            if nums[j - 1] >= nums[j]:
                break
            j -= 1
        return ans


        # # Initialize the index for traversing the array from the beginning
        # left_index = 0
        # array_size = len(nums)
      
        # # Find the first decreasing point in the array
        # # Increment left_index as long as the next element is greater than the current
        # while left_index + 1 < array_size and nums[left_index] < nums[left_index + 1]:
        #     left_index += 1
      
        # # If the whole array is strictly increasing, then all subarrays are "incremovable"
        # if left_index == array_size - 1:
        #     # Calculate the total number of subarrays using the formula for the sum of the first N natural numbers
        #     return array_size * (array_size + 1) // 2
      
        # # Initialize answer with the case where we consider the longest increasing subarray from the start
        # answer = left_index + 2
      
        # # Start iterating the array from the end
        # right_index = array_size - 1
        # while right_index:
        #     # Decrease left_index until we find an element smaller than the one at right_index
        #     while left_index >= 0 and nums[left_index] >= nums[right_index]:
        #         left_index -= 1
          
        #     # Add the number of "incremovable" subarrays ending at current right_index
        #     answer += left_index + 2
          
        #     # Break the loop if the subarray is not strictly increasing anymore
        #     if nums[right_index - 1] >= nums[right_index]:
        #         break
          
        #     # Move the right index to the left
        #     right_index -= 1
      
        # # Return the total count of "incremovable" subarrays
        # return answer

