class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # # XOR operation to find the bits that are different between start and goal
        # different_bits = start ^ goal
      
        # # Initialize the count of bit flips required to 0
        # ans = 0
      
        # # Count the number of bits set to 1 in different_bits
        # while different_bits:
        #     # Increment the counter if the least significant bit is 1
        #     ans += different_bits & 1
        #     # Right-shift to check the next bit
        #     different_bits >>= 1
      
        # # Return the total count of flips needed
        # return ans

        ###### number of different bits ############
        xor = start ^ goal
        # return str(bin(xor)).count('1')
        ans = 0
        while xor:
            ans += xor & 1
            xor >>= 1
        return ans


        # s = bin(start)[2:][::-1]
        # g = bin(goal)[2:][::-1]
        # ans = 0
        # i = 0
        # while i < min(len(s), len(g)):
        #     if s[i] != g[i]:
        #         ans += 1
        #     i += 1
        # if len(s) < len(g):
        #     ans += g[i:].count('1')
        # else:
        #     ans += s[i:].count('1')
        # return ans