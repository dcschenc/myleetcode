class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0300-0399/0375.Guess%20Number%20Higher%20or%20Lower%20II
        @cache
        def min_cost(start, end):
            if start >= end:
                return 0
            # if dp[start][end] != 0:
            #     return dp[start][end]

            min_guess = float('inf')
            for guess in range(start, end + 1):
                cost = guess + max(min_cost(start, guess - 1), min_cost(guess + 1, end))
                min_guess = min(min_guess, cost)

            # dp[start][end] = min_guess
            return min_guess

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        return min_cost(1, n)        