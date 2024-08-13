class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # https://algo.monster/liteproblems/2901
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2901.Longest%20Unequal%20Adjacent%20Groups%20Subsequence%20II

        # Helper function to check if two strings s and t differ by exactly one character
        def is_one_letter_diff(s: str, t: str) -> bool:
            return len(s) == len(t) and sum(a != b for a, b in zip(s, t)) == 1
        
        n = len(words)
        # Initialize a list to store the length of the longest subsequence ending at each word
        lengths = [1] * n
        # Initialize a list to store the previous index for the longest subsequence
        previous_index = [-1] * n
        # Variable to store the length of the longest subsequence found so far
        max_length = 1
      
        # Iterate through each word
        for i, current_group in enumerate(groups):
            # Compare with every other word before it
            for j, previous_group in enumerate(groups[:i]):
                # If the groups are different, and the length can be increased, and the words differ by one letter
                if (current_group != previous_group and lengths[i] < lengths[j] + 1 and is_one_letter_diff(words[i], words[j])):
                    # Update the length of the longest subsequence ending at the current word
                    lengths[i] = lengths[j] + 1
                    # Update the previous index to the current longest subsequence
                    previous_index[i] = j
                    # Update the maximum length of the longest subsequence found
                    max_length = max(max_length, lengths[i])

        # Initialize a list to store the words of the longest subsequence
        longest_subsequence = []
      
        # Iterate through each word to find the end of the longest subsequence
        for i in range(n):
            if lengths[i] == max_length:
                j = i
                # Backtrack through the previous indices to construct the longest subsequence
                while j >= 0:
                    longest_subsequence.append(words[j])
                    j = previous_index[j]
                break
        # Return the longest subsequence in the correct order
        return longest_subsequence[::-1]
