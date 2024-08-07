class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        prize_positions = prizePositions
        # Get the number of available positions
        num_positions = len(prize_positions)
        # Initialize the dp (dynamic programming) array with zeroes
        dp = [0] * (num_positions + 1)
        # 'max_win' will store the maximum number of wins attainable
        max_win = 0
      
        # Iterate through the prize positions
        for i, position in enumerate(prize_positions, 1):
            # Find the leftmost position in 'prize_positions' where the player could have been
            # to ensure the distance between consecutive prizes is at most 'k'
            j = bisect_left(prize_positions, position - k)
          
            # The current win is calculated by previous win at 'j' plus the number of positions
            # between 'j' and the current position 'i', update 'max_win' accordingly
            max_win = max(max_win, dp[j] + i - j)
          
            # Update the dp array with the maximum of the previous value or the new calculated win
            dp[i] = max(dp[i - 1], i - j)
      
        # Finally, return the maximum number of wins after processing all positions
        return max_win        