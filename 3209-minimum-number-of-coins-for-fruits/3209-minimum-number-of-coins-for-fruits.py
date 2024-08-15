class Solution:
    def minimumCoins(self, prices: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2944.Minimum%20Number%20of%20Coins%20for%20Fruits
        @cache
        def dfs(i: int) -> int:
            if i * 2 >= len(prices):
                return prices[i - 1]
            return prices[i - 1] + min(dfs(j) for j in range(i + 1, i * 2 + 2))

        return dfs(1)