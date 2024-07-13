class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n % 2 == 1:
            ans.append(0)
            n = n - 1
        i = 1
        while n > 0:
            ans.append(i)
            ans.append(-i)
            i += 1
            n -= 2
        return ans
