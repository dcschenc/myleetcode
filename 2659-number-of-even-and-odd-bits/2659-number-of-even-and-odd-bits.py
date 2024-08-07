class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        # n = bin(n)[2:]
        # odd, even = 0, 0
        # for i, c in enumerate(n[::-1]):
        #     if c == '1' and i % 2 == 0:
        #         even += 1
        #     if c == '1' and i % 2 == 1:
        #         odd += 1
        # return [even, odd]

        odd, even = 0, 0
        i = 0
        while n:
            if n & 1 == 1:
                if i & 1 == 0:
                    even += 1
                else:
                    odd += 1
            i += 1
            n >>= 1
        return [even, odd]
        