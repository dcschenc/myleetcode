class Solution:
    def countHousePlacements(self, n: int) -> int:
        # Define the modulo constant to handle large numbers.
        MOD = 10**9 + 7

        # f represents the count of ways to place houses such that
        # the last plot is empty.
        f = [1] * n
      
        # g represents the count of ways to place houses such that
        # the last plot is occupied.
        g = [1] * n

        # Iterate over the plots starting from the second one.
        for i in range(1, n):
            # If the last plot is empty, then it must come after an occupied plot.
            f[i] = g[i - 1]
          
            # If the last plot is occupied, it can come after either
            # an empty plot or another occupied plot.
            g[i] = (f[i - 1] + g[i - 1]) % MOD

        # v is the total number of ways to place houses on the last plot.
        v = f[-1] + g[-1]

        # Since we can independently choose how to place houses on each side of the street,
        # we square the number of ways to find the total combinations.
        # We return the result modulo MOD to handle large numbers.
        return (v * v) % MOD
