class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1918.Kth%20Smallest%20Subarray%20Sum
        # Helper function to check if the count of subarrays with sum less than or equal to 'limit'
        # is at least k
        def has_k_or_more_subarrays_with_sum_at_most(limit):
            total_sum = 0  
            start = 0  
            count = 0  # Count of subarrays with sum less than or equal to 'limit'
            # Iterate over the numbers in the array
            for end, num in enumerate(nums):
                total_sum += num
                # Shrink the window from the left if the total sum exceeds the limit
                while total_sum > limit:
                    total_sum -= nums[start]
                    start += 1
                # The count is increased by the number of subarrays ending with nums[end]
                count += end - start + 1
            # Check if we have at least k subarrays
            return count >= k

        # Binary search to find the kth smallest subarray sum
        left, right = min(nums), sum(nums)
        # Perform binary search with a custom key function by using the bisect_left function
        kth_smallest_sum = left + bisect_left(range(left, right + 1), True, key=has_k_or_more_subarrays_with_sum_at_most)
        return kth_smallest_sum  