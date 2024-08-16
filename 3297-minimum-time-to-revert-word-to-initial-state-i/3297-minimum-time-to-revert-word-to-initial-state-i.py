class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3029.Minimum%20Time%20to%20Revert%20Word%20to%20Initial%20State%20I
        # Calculate the length of the word

        # https://algo.monster/liteproblems/3029
        
        word_length = len(word)
      
        # Iterate over the word, checking substrings of length multiples of k
        for i in range(k, word_length, k):
            # Check if the substring from the current position to the end
            # matches the substring from the beginning to the complementary position
            if word[i:] == word[:-i]:
                # If yes, the minimum number of times to reach the initial state can be calculated
                # by dividing the current index by k. Return this value.
                return i // k
      
        # If no pattern was found, calculate and return the ceiling division of the
        # word's length by k, as the number of times needed to process the entire string
        return (word_length + k - 1) // k

        # n = len(word)
        # longest = 0
        # for i in range(n):
        #     l = i
        #     if word[:i + 1] == word[-(i + 1):] and l % k == 0 and l != n - 1:
        #         longest = i
        
        # return (n - longest) // k