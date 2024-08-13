class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        # https://algo.monster/liteproblems/2875
        total_sum = sum(nums)  # Calculate the total sum of all numbers in the array
        num_count = len(nums)  # Get the length of the array

        # Initialize an 'a' which is the number of complete array rotations required
        num_full_rotations = 0
        if target > total_sum:
            num_full_rotations = (target // total_sum) * num_count
            target -= (target // total_sum) * total_sum  # Update the target after the full rotations

        # If target equals total_sum, return the array length
        if target == total_sum:
            return num_count

        pos = {0: -1}  # Create a dictionary to store the prefix sum indices
        prefix_sum = 0  # Initialize the prefix sum
        min_length = inf  # Set initial min length to infinity

        # Traverse through the array
        for i, num in enumerate(nums):
            prefix_sum += num  # Update prefix sum

            # Check if there's a subarray that ends at index i with sum equals target
            if (t := prefix_sum - target) in pos:
                min_length = min(min_length, i - pos[t])

            # Check if there is a circular subarray that sums to target
            if (t := prefix_sum - (total_sum - target)) in pos:
                min_length = min(min_length, num_count - (i - pos[t]))

            # Store the latest index of this prefix sum
            pos[prefix_sum] = i

        # If min_length is still infinity, no subarray was found. Return -1.
        # Otherwise, return the answer which includes the rotations 'a' + the found subarray length 'b'
        return -1 if min_length == inf else num_full_rotations + min_length

        # total = sum(nums)
        # nums = nums * max(2, (target // total + 10))
        # i, n = -1, len(nums)
        # cur, ans = 0, float('inf')
        # hm = {}
        # for i in range(n):
        #     cur += nums[i]
        #     if cur - target in hm:
        #         ans = min(ans, i - hm[cur - target])
        #     hm[cur] = i
        # return ans if ans != float('inf') else -1

        # print(nums)
        # while i < n:
        #     j = i + 1
        #     while j < n and cur < target:
        #         cur += nums[j]
        #         j += 1
        #     if cur == target:
        #         ans = min(ans, j - i + 1)    
        #         i += 1        
        #     else:
        #         k = i + 1
        #         while k < n and cur > target:
        #             cur -= nums[k]
        #             k += 1
        #         if cur == target:
        #             ans = min(ans, j - k + 1)
        #         i = k
        # return ans if ans != float('inf') else -1

            