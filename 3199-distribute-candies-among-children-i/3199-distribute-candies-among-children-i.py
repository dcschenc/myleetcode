class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        total = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                if 0 <= n - (i + j) <= limit:
                    total += 1
        return total