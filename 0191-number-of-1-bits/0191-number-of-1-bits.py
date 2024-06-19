class Solution:
    def hammingWeight(self, n: int) -> int:
        # bstr = bin(n)
        # cnt = 0
        # for c in bstr:
        #     if c == '1':
        #         cnt += 1
        # return cnt

        count = 0
        while n:
            # count += n%2
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count