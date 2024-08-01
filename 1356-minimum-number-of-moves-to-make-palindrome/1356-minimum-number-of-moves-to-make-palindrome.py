class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2193.Minimum%20Number%20of%20Moves%20to%20Make%20Palindrome
        # Convert the string into a list for easy manipulation.
        char_list = list(s)
        # Initialize the number of moves and the indexes.
        moves = 0
        n = len(s)
        left = 0
        right = n - 1

        # Iterate until we have checked all characters.
        while left < right:
            # Flag to check if we found a matching character.
            found = False

            # Iterate from right to left starting from the current right index,
            # looking for a matching character.
            for k in range(right, left, -1):
                if char_list[left] == char_list[k]:
                    # When we find a match, we set found to True.
                    found = True
                    # We then move the matched character to its correct position
                    # by swapping adjacent characters.
                    while k < right:
                        char_list[k], char_list[k + 1] = char_list[k + 1], char_list[k]
                        k += 1
                        # Increment the moves count for each swap.
                        moves += 1
                    # Once we have moved the character to the correct position,
                    # we decrement the right index.
                    right -= 1
                    break

            # If we did not find a matching character, it means
            # the character needs to be moved to the center for odd length palindrome.
            if not found:
                # For this unmatched character, how many moves will it take to reach the center?
                # It will be half the length of the string minus the current index.
                moves += (n // 2) - left

            # Move to the next character from the left.
            left += 1

        # Return the total number of moves required to form a palindrome.
        return moves
        