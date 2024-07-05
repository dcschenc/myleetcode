class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        for i, d in enumerate(num[::-1]):
            n = n + d * (10**i)
        n += k
        ans = []
        while n > 0:
            ans.append(n % 10)
            n = n // 10
        return ans[::-1]