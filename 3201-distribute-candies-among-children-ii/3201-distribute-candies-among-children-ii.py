class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for i in range(min(n, limit)+1):
           remain = n - i
           lower = max(0, remain - limit)
           higher = min(limit, remain)
           if higher >= lower:
                total += (higher - lower + 1)
        return total 