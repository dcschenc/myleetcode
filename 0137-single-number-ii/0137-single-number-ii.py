class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ######## method 1 #########
        bits = [0]*32
        cnt = 0
        for num in nums:
            bstr = bin(num)
            if bstr[0] == '-':
                cnt += 1
                bstr = bstr[3:]
            else:
                bstr = bstr[2:]
             
            for i, c in enumerate(bstr[::-1]):
                if c == '1':
                    bits[i] += 1
                    
        for i in range(len(bits)):            
            bits[i] = bits[i] % 3
        res = int('0b' + ''.join([str(x) for x in bits[::-1]]), 2)
        if cnt % 3 != 0:
            return -res
        return res

        ### method 2 #####
        # Loner.
        loner = 0

        # Iterate over all bits
        for shift in range(32):
            bit_sum = 0
            # For this bit, iterate over all integers
            for num in nums:
                # Compute the bit of num, and add it to bit_sum
                bit_sum += (num >> shift) & 1
            # Compute the bit of loner and place it
            loner_bit = bit_sum % 3
            loner = loner | (loner_bit << shift)
        # Do not mistaken sign bit for MSB.
        if loner >= (1 << 31):
            loner = loner - (1 << 32)

        return loner

    ###### method 3 #######
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for key in freq:
            if freq[key] == 1:
                return key