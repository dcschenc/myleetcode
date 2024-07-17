class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1493.Longest%20Subarray%20of%201's%20After%20Deleting%20One%20Element
        n = len(nums)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for i, x in enumerate(nums, 1):
            if x:
                left[i] = left[i - 1] + 1
        for i in range(n - 1, -1, -1):
            if nums[i]:
                right[i] = right[i + 1] + 1
        return max(left[i] + right[i + 1] for i in range(n))

        max_length = 0  # Initialize the maximum length of the subarray
        left = 0        # Initialize the left pointer of the window
        zero_count = 0  # Initialize a count for the number of zeros in the window

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1  # Increment the zero count

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Shrink the window

            max_length = max(max_length, right - left)  # Update the maximum length

        return max_length


        # n = len(nums)
        # max_n, curr = 0, 0
        # last_idx = 0
        # seen = False
        # for i in range(n):
        #     if nums[i] == 1:
        #         curr+=1
        #     else:                
        #         if seen:                    
        #             curr = i-last_idx
        #             last_idx = i                   
        #         else:
        #             curr +=1
        #         last_idx = i        
        #         seen = True
        #     if curr > max_n:
        #         max_n = curr
        # return max_n - 1