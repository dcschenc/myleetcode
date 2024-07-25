class Solution:
    def sumBase(self, n: int, k: int) -> int:
        ans = 0
        while n > 0:
            mod = n % k
            n = n // k
            ans += mod
        return ans
        