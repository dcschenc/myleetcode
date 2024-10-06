class Solution:
    def minFlips(self, s: str) -> int:
        # https://algo.monster/liteproblems/1888
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1888.Minimum%20Number%20of%20Flips%20to%20Make%20the%20Binary%20String%20Alternating
        
        # Determine the length of the input string "s"
        n = len(s)
      
        # This string will be used to check against the input string "s"
        target = "01"
      
        # Count the number of flips required to match the "01" pattern starting with "0"
        initial_flips = sum(char != target[i % 2] for i, char in enumerate(s))
      
        # Initialize the minimum flips answer with the minimum between
        # matching "01" or "10" pattern starting with "0"
        min_flips = min(initial_flips, n - initial_flips)
      
        # Loop over the string "s" to consider all cyclic permutations of "s"
        for i in range(n):
            # On each iteration, consider that the first character has moved to the end
            # Adjust the flip count accordingly
            # initial_flips -= s[i] != target[i % 2]
            # initial_flips += s[i] != target[(i + n) % 2]
            if s[i] != target[i % 2]:
                initial_flips -= 1
            if s[i] != target[(i + n) % 2]:
                initial_flips += 1
          
            # Update the minimum flips answer considering the current cyclic permutation
            min_flips = min(min_flips, initial_flips, n - initial_flips)
          
        # Return the minimum flips answer found
        return min_flips
