class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Initialize the answer and the smallest absolute difference.
        closest_number = 0
        smallest_diff = float('inf')
      
        # Iterate through each number in the list.
        for num in nums:
            # Calculate the absolute difference of the current number.
            current_diff = abs(num)
          
            # If the absolute difference is smaller than the smallest difference found so far,
            # or if the absolute difference is equal but the number is greater (closer to zero),
            # update the answer and the smallest difference.
            if current_diff < smallest_diff or (current_diff == smallest_diff and num > closest_number):
                closest_number = num
                smallest_diff = current_diff
      
        # Return the number that is closest to zero.
        return closest_number