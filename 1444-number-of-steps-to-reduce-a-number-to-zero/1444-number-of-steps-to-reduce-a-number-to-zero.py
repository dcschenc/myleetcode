class Solution:
    def numberOfSteps(self, num: int) -> int:
        # steps = 0
        # while num > 0:
        #     steps += 1
        #     if num%2 == 0:                
        #         num /= 2
        #     else:
        #         num -= 1
        # return steps
        
        steps = 0
        while num > 0:
            steps += 1
            if num & 1 == 0:
                num >>= 1
            else:
                num -= 1
        return steps

        steps = 0

        # Get the binary for num, as a String. Remove the "0b" off the start with splice.
        binary = bin(num)[2:]
        
        # Iterate over all the bits in the binary string.
        for bit in binary:
            # Must use "1", not 1 here. The bits are strings!
            if bit == "1": # If the bit is a 1 
                steps = steps + 2 # Then it'll take 2 to remove.
            else: # bit == "0"
                steps = steps + 1 # Then it'll take 1 to remove.

        # We need to subtract 1, because the last bit was over-counted.
        return steps - 1