class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ones = None
        while n:
            if n & 1 == 1:
                if ones is None or ones is False:
                    ones = True                
                else:
                    return False
            else:
                if ones is None or ones is True:                 
                    ones = False
                else:
                    return False
            n >>= 1
        return True