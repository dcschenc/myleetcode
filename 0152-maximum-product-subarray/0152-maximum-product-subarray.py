class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_product = [nums[0]] * n
        min_product = [nums[0]] * n
        for i in range(1, n):
            max_product[i] = max(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])
            min_product[i] = min(nums[i], max_product[i-1]*nums[i], min_product[i-1]*nums[i])

        return max(max_product)
        
        # The key intuition is that dynamic programming is used to keep track of the maximum   and minimum product ending at each position and update them based on the previous values, ensuring that the algorithm considers various scenarios to find the maximum product subarray
        if not nums:
            return 0

        max_product_ending_here = nums[0]
        min_product_ending_here = nums[0]

        max_product = nums[0]

        for i in range(1, len(nums)):
            # Store the current maximum product in a temporary variable
            temp = max_product_ending_here

            # Update the maximum and minimum products ending at the current position
            max_product_ending_here = max(nums[i], max_product_ending_here * nums[i], min_product_ending_here * nums[i])
            min_product_ending_here = min(nums[i], temp * nums[i], min_product_ending_here * nums[i])

            # Update the overall maximum product
            max_product = max(max_product, max_product_ending_here)

        return max_product





        