class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        cnt = 0
        while z:
            if z & 1:
                cnt += 1
            z >>= 1
        return cnt