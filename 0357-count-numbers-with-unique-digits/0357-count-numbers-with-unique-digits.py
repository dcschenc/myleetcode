class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # if n == 0:
        #     return 1
        # if n == 1:
        #     return 10
        # ans, cur = 10, 9
        # for i in range(n - 1):
        #     cur *= 9 - i
        #     ans += cur
        # return ans

        # if n == 0:
        #     return 1
        # # Initialize the dp array with base case for n = 1
        # dp = [0] * (n + 1)
        # dp[1] = 10  # For n = 1, there are 10 numbers with unique digits (0 to 9)

        # # Fill the dp array using the recurrence relation
        # for i in range(2, min(n, 10) + 1):
        #     unique_digits = 9
        #     available_digits = 9
        #     for j in range(2, i + 1):
        #         unique_digits *= available_digits
        #         available_digits -= 1
        #     dp[i] = dp[i - 1] + unique_digits

        # return dp[n]

        def backtrack(idx):
            nonlocal count
            count += 1
            if idx == n:
                return
            for d in '0123456789':
                if idx == 0 and d == '0':
                    continue 
                if d not in path:
                    path.append(d)
                    backtrack(idx + 1)
                    path.pop()  # not path.pop(d)

        count = 0      
        path = []
        backtrack(0)
        return count