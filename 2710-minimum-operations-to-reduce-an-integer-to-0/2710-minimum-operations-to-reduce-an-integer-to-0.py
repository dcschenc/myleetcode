class Solution:
    def minOperations(self, n: int) -> int:
        # Initialize operations count (ops) and a counter for consecutive ones (consecutive_ones).
        ops = 0
        consecutive_ones = 0
      
        # Process all bits of the integer n from right to left (LSB to MSB).
        while n:
            # Check if the least significant bit (LSB) is 1.
            if n & 1:
                # If it is, increase the counter for consecutive ones.
                consecutive_ones += 1
            # If it is 0 and the counter for consecutive ones is not zero.
            elif consecutive_ones:
                # A zero after some ones means a completed set of "10" or "110." 
                # Operation needed to convert this set to "00" or "100".
                ops += 1
                # Reset the counter for consecutive ones.
                # '1' in binary is already minimized, and for '11' we only need one operation
                # to change it to '10' and then we 'carry the 1' so to speak.
                consecutive_ones = 0 if consecutive_ones == 1 else 1
          
            # Right shift n by 1 to check the next bit.
            n >>= 1
      
        # If there is a residual 1 then an operation is needed; 
        # this could be a trailing '1' or '10' after the end of the loop.
        if consecutive_ones == 1:
            # Increment the operations count by 1.
            ops += 1
        # If there are more than 1 ones, an extra operation is needed to handle the carry.
        elif consecutive_ones > 1:
            # Increment the operations count by 2. This is the case for '11' in binary,
            # where one operation is to change '11' to '10' and second operation to change
            # '10' to '00'.
            ops += 2
      
        # Return the number of operations required.
        return ops

        
        def dfs(n):
            v = int(math.log(n, 2))  # O(1)
            if n == pow(2, v): # O(1)
                return 1            
  
            low = 2 ** v
            high = 2 ** (v + 1)

            d1 = n - low
            d2 = high - n

            return 1 + min(dfs(d1), dfs(d2))
        
        return dfs(n)