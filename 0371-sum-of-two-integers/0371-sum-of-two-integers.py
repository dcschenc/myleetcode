class Solution:
    def getSum(self, a: int, b: int) -> int:
        # https://algo.monster/liteproblems/371
        # Mask to get 32-bit representation
        mask = 0xFFFFFFFF      
        # Convert a and b to 32-bit integers
        a, b = a & mask, b & mask      
        print(a, b)  # a become 4294967295, 1111 1111 1111 1111 1111 1111 1111 1111
        # Iterate while there is a carry
        while b:
            # Calculate the carry from a and b,
            # and ensure it's within the 32-bit boundary
            carry = ((a & b) << 1) & mask          
            # XOR a and b to find the sum without considering carries,
            # then consider the carry for the next iteration
            a, b = a ^ b, carry
            print(a, b, carry)
        # if a < 0x80000000:
        if a <= 0x7FFFFFFF: # largest positive integer
            return a
      
        # If a is outside the 32-bit integer range, which means it is negative,
        # return the two's complement negative value, which is the bitwise negation of a
        # (by XORing with MASK, which is 'all 1's for a 32-bit number') and adding 1
        return ~(a ^ mask)

        # https://github.com/doocs/leetcode/tree/main/solution/0300-0399/0371.Sum%20of%20Two%20Integers
        
        mask = 0xFFFFFFFF        
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        max_int = 0x7FFFFFFF
        return a if a < max_int else ~(a ^ mask)
        