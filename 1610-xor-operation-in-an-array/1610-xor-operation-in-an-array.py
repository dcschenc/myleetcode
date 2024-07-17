class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(xor, ((start + 2 * i) for i in range(n)))
        
        ans = start
        for i in range(1, n):
            ans ^= (start + 2 * i)
        return ans
            