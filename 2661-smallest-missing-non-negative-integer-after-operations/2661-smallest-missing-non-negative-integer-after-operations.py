class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # https://algo.monster/liteproblems/2598
        # Create a counter to keep track of the frequency of each number modulo 'value'
        modulo_counter = Counter(num % value for num in nums)
      
        # Iterate over the numbers from 0 to length of nums (inclusive)
        for i in range(len(nums) + 1):
            # If there is no number i modulo 'value' in our collection, return i
            if modulo_counter[i % value] == 0:
                return i
            # Otherwise, decrease the count of i modulo 'value' by one
            modulo_counter[i % value] -= 1
