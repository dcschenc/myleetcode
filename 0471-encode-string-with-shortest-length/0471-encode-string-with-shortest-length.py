class Solution:
    def encode(self, s: str) -> str:
        # Helper method to compute the encoded string for a substring s[i:j+1]
        def compute_encoded_substring(start: int, end: int) -> str:
            substring = s[start:end + 1]
            # If the substring is too short, encoding doesn't make sense, return as is
            if len(substring) < 5:
                return substring
          
            # Try to find a repeated pattern in the substring
            duplicate_index = (substring + substring).find(substring, 1)
          
            # If a repeated pattern is found that's shorter than the original string
            if duplicate_index < len(substring):
                count_of_repetition = len(substring) // duplicate_index
                # Encoded format: count[encoded substring for the repeated pattern]
                return f"{count_of_repetition}[{dp[start][start + duplicate_index - 1]}]"
            # No repeated pattern was found, return the original substring
            return substring

        # Main logic begins here
        n = len(s)
        # Initialize dynamic programming table with None
        dp = [[None] * n for _ in range(n)]
      
        # Build the table bottom-up
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # Compute encoded substring for current i, j
                dp[i][j] = compute_encoded_substring(i, j)
              
                # If current substring can potentially be shortened
                if j - i + 1 > 4:
                    # Try to break the substring into two parts and see if this gives
                    # a shorter encoding by checking all possible split positions
                    for k in range(i, j):
                        # Combine encoded substrings for both parts
                        trial_encoded = dp[i][k] + dp[k + 1][j]
                        # If this combination gives us a shorter string, update the table
                        if len(dp[i][j]) > len(trial_encoded):
                            dp[i][j] = trial_encoded
      
        # Result is in the top-right cell of the dynamic programming table
        return dp[0][-1]        