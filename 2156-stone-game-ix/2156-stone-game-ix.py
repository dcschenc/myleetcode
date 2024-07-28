class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # starting with a stone that leaves a remainder of either 1 or 2 when divided by 3
        def can_alice_win(counts):
            # Alice loses immediately if there are no stones that leave a remainder of 1 when divided by 3
            if counts[1] == 0:
                return False
            counts[1] -= 1
            # Calculate the initial turn and simulate the game by adding stones
            # that leave a remainder of 0 when divided by 3 or twice the minimum
            # of stones leaving remainders of 1 or 2
            turn_count = 1 + min(counts[1], counts[2]) * 2 + counts[0]
            # If there are more stones with remainder 1, add another turn
            # (Alice picks one more of these stones)
            if counts[1] > counts[2]:
                turn_count += 1
                counts[1] -= 1
            # Alice wins if the final turn count is odd and there's no equal amount
            # of stones with remainders 1 and 2 after all possible selections
            return turn_count % 2 == 1 and counts[1] != counts[2]

        # Initialize an array to count stones based on their remainder when divided by 3
        remainder_counts = [0] * 3
        for stone in stones:
            remainder_counts[stone % 3] += 1
        # Create a variant of this array to simulate starting with a remainder of 2
        swapped_remainder_counts = [remainder_counts[0], remainder_counts[2], remainder_counts[1]]
      
        # Return True if Alice can win by starting with a remainder of 1 or 2
        return can_alice_win(remainder_counts) or can_alice_win(swapped_remainder_counts)