class Solution:
    def findComplement(self, num: int) -> int:
        n = len(bin(num)) - 2
        mask = 2 ** n - 1
        return num ^ mask

        # n is a length of num in binary representation
        n = floor(log2(num)) + 1      
        # The bitmask has the same length as num and contains only ones 1...1
        bitmask = (1 << n) - 1
        # Flip all bits
        return bitmask ^ num

        todo, bit = num, 1
        while todo:
            # flip the current bit
            num = num ^ bit
            # prepare for the next run
            bit = bit << 1
            todo = todo >> 1
        return num