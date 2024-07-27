class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        # Apply memoization to avoid recomputation of the same game states
        @lru_cache(maxsize=None)
        def dfs(st):
            # Convert tuple to list to modify the piles
            piles_list = list(st)
            # Iterate over each pile
            for i, pile in enumerate(piles_list):
                # Try removing 1 to pile stones from the current pile
                for stones_removed in range(1, pile + 1):
                    # Remove the stones for the current move
                    piles_list[i] -= stones_removed
                    # Check if opponent would lose from this state
                    if not dfs(tuple(piles_list)):
                        return True  # If opponent loses, current player wins
                    # Undo the move
                    piles_list[i] += stones_removed
            # If no winning move, return False
            return False

        # Start the game with the initial piles configuration
        return dfs(tuple(piles))