class Solution:
    def houseOfCards(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2189.Number%20of%20Ways%20to%20Build%20House%20of%20Cards
        @cache
        def dfs(n: int, k: int) -> int:
            # where k is the current row's triangle count. This formula comes from the fact that 
            # each additional triangle in a row requires 3 more cards than the previous triangle 
            # (2 cards for the triangle itself and 1 card for the horizontal separator).
            x = 3 * k + 2
            if x > n:
                return 0
            if x == n:
                return 1
            return dfs(n - x, k + 1) + dfs(n, k + 1)

        return dfs(n, 0)

        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2189.Number%20of%20Ways%20to%20Build%20House%20of%20Cards
        @cache
        def dfs(n: int, k: int) -> int:
            x = 3 * k + 2
            if x > n:
                return 0
            if x == n:
                return 1
            return dfs(n - x, k + 1) + dfs(n, k + 1)

        return dfs(n, 0)