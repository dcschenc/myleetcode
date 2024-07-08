class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        m = n
        ans = 0
        while m > 0:
            mod = m % 10
            ans += mod ** k
            m = m // 10
        return ans == n