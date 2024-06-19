class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret
        
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res |= (bit << (31 - i))
        return res
        
        # # print(n)
        # bstr = list(bin(n))
        # i, j = 2, len(bstr)-1
        # while i < j:
        #   bstr[i], bstr[j] = bstr[j], bstr[i]
        #   i+=1
        #   j-=1
        # if len(bstr) < 34:
        #   bstr.extend(['0'] * (34-len(bstr)))
        # return int("".join(bstr), 2)