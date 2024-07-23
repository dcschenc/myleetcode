class Solution:
    def totalMoney(self, n: int) -> int:
        total = sum([i for i in range(1, 8)])
        ans = 0
        if n >= 7:
            ans = total
        weeks = n // 7
        mod = n % 7
        for i in range(1, weeks):
            total = total + 7
            ans += total
        days = weeks + 1
        for i in range(1, mod+1):
            ans += days
            days += 1
        return ans