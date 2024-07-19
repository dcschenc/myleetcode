class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        ans, n = 0, len(piles)
        i, j = 0, n - 1
        cnt = 1
        while cnt <= n // 3:
            ans += piles[2 * cnt - 1]
            cnt += 1
        return ans

        