class Solution:
    def stoneGame(self, piles: List[int]) -> bool:   
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0877.Stone%20Game 
        n = len(piles)
        # Initialize a 2D array to store the maximum difference in scores
        # between the player who starts and the other player, for any given pile range
        dp = [[0] * n for _ in range(n)]
      
        # Fill the array along the main diagonal, where each cell
        # on the diagonal represents only one pile
        for i, pile in enumerate(piles):
            dp[i][i] = pile

        # Dynamic programming - bottom-up approach, filling the table
        # Start from second last row and go upwards
        for i in range(n - 2, -1, -1):
            # For each row, start from the element right to the diagonal element and move rightwards
            for j in range(i + 1, n):
                # dp[i][j] will be the maximum difference in score achievable by the player who starts
                # i.e., max of choosing the left-most or right-most pile
                # The decision is whether to take the pile at the current left (piles[i])
                # minus what the opponent would get (dp[i + 1][j]),
                # or to take the pile at the current right (piles[j])
                # minus what the opponent would get (dp[i][j - 1])
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])
      
        # The first player wins if the maximum difference in score is positive
        return dp[0][n - 1] > 0

        @cache
        def dp(left, right):
            if left == right:
                return piles[left]

            # The current player can either pick piles[left] or piles[right]
            choose_left = piles[left] - dp(left + 1, right)
            choose_right = piles[right] - dp(left, right - 1)

            # The player chooses the option that maximizes their score
            return max(choose_left, choose_right)
        n = len(piles)

        # Check if the first player's score is non-negative
        return dp(0, n - 1) >= 0
        

        @cache
        def dp(left, right):
            if right - left  == 1:
               return max(piles[left], piles[right])
        
            choose_left = piles[left] + max(dp(left + 1, right - 1), dp(left + 2, right))
            choose_right = piles[right] + max(dp(left, right - 2), dp(left + 1, right - 1))
            return max(choose_left, choose_right)
        
        n = len(piles)
        alice = dp(0, n-1)
        return alice > sum(piles)//2