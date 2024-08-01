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

        # Define a decorated helper function with memoization 
        # to avoid redundant computations.
        @lru_cache(maxsize=None)
        def dfs(remaining_cards: int, level: int) -> int:
            # Calculate the number of cards required to build 
            # the next level of the house.
            required_cards = 3 * level + 2

            # Check if the required cards exceed the remaining cards.
            if required_cards > remaining_cards:
                return 0  # No more levels can be built, so return 0.
          
            # Check if the remaining cards exactly match the required cards.
            if required_cards == remaining_cards:
                return 1  # Found a solution where all cards are used, return 1.
          
            # Calculate two scenarios:
            # 1. Building the next level and checking the remaining cards
            # 2. Skipping the current level and trying the next one
            return (dfs(remaining_cards - required_cards, level + 1) + 
                    dfs(remaining_cards, level + 1))

        # Start the recursive process with all cards available and starting 
        # from the 0th level.
        return dfs(n, 0)   