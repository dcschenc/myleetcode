class Solution:
    def toHex(self, num: int) -> str:
        # if num == 0: return '0'      
        # hex_chars = '0123456789abcdef'      
        # hex_string = []
      
        # # We extract 4 bits at a time from the integer, and we process from the MSB to the LSB
        # # On a 32-bit architecture, we process the integer as 8 groups of 4 bits.
        # for i in range(7, -1, -1):
        #     # Extract 4 bits by shifting right (4 * position) and masking with 0xF to get the value
        #     current_bits = (num >> (4 * i)) & 0xF
          
        #     # If the hex_string list is non-empty or the current_bits are non-zero, append the corresponding hex character
        #     # This check also prevents leading zeros from being included in the output
        #     if hex_string or current_bits != 0:
        #         hex_string.append(hex_chars[current_bits])
      
        # # Join the list into a string and return it as the hexadecimal representation
        # return ''.join(hex_string)

        # hm = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        hexchar = '0123456789abcdef'
        res = ''
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        while num > 0:
            mod = num % 16
            num = num // 16
            res += hexchar[mod]
            # if mod < 10:
            #     res += str(mod)
            # else:
            #     res += hm[mod]
        return res[::-1]