class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Initialize the prefix sum as zero
        prefix_sum = 0
      
        # A dictionary to keep track of the earliest index where 
        # a particular modulus (prefix_sum % k) is found.
        mod_index_map = {0: -1}  # The modulus 0 is at the "imaginary" index -1
      
        # Iterate over the list of numbers
        for index, value in enumerate(nums):
            # Update the prefix sum with the current value
            prefix_sum += value
          
            # Get the modulus of the prefix sum with 'k'
            modulus = prefix_sum % k
          
            # If the modulus has been seen before and the distance between 
            # the current index and the earlier index of the same modulus 
            # is at least 2, we found a subarray sum that's multiple of k
            if modulus in mod_index_map and index - mod_index_map[modulus] >= 2:
                return True
          
            # Store the index of this modulus if it's not seen before
            if modulus not in mod_index_map:
                mod_index_map[modulus] = index
      
        # No subarray found that sums up to a multiple of k
        return False


        # n = len(nums)
        # presum = [0] * (n + 1)
        # for i, num in enumerate(nums):
        #     presum[i + 1] = presum[i] + num
        # # print(presum)
        # for i in range(n + 1):
        #     for j in range(i + 2, n + 1):
        #         if (presum[j] - presum[i]) % k == 0:
        #             # print(i, j)
        #             return True
        # return False