from collections import Counter
# https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0792.Number%20of%20Matching%20Subsequences
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0792.Number%20of%20Matching%20Subsequences
        d = defaultdict(deque)
        for w in words:
            d[w[0]].append(w)
        ans = 0
        for c in s:
            for _ in range(len(d[c])):
                t = d[c].popleft()
                if len(t) == 1:
                    ans += 1
                else:
                    d[t[1]].append(t[1:])
        return ans

        # Initialize a dictionary to hold queues of tuples for each character in words.
        # Each tuple contains an index of a word in words and the next character index to search for.
        char_to_word_indices = defaultdict(deque)      
        # Populate the dictionary with initial character indices for each word.
        for index, word in enumerate(words):
            char_to_word_indices[word[0]].append((index, 0))
      
        # Counter for the number of matching subsequences found.
        matching_count = 0
      
        # Loop through each character in the input string.
        for char in s:
            # Process all tuples (word index, character index) for the current character.
            for _ in range(len(char_to_word_indices[char])):
                word_index, char_index = char_to_word_indices[char].popleft()
                char_index += 1  # Move to the next character in the current word
          
                # If we reached the end of the word, increment the count of matching subsequences.
                if char_index == len(words[word_index]):
                    matching_count += 1
                else:
                    # Else, append the tuple (word index, next character index) to the appropriate list.
                    next_char = words[word_index][char_index]
                    char_to_word_indices[next_char].append((word_index, char_index))
      
        # Return the total count of matching subsequences.
        return matching_count


        # def is_subsequence(w):            
        #     i, j = 0, 0
        #     while i < len(w) and j < len(s):
        #         if w[i] == s[j]:
        #             i += 1
        #             j += 1
        #         else:
        #             j += 1
        #     return i == len(w)
        
        # # s_counter = Counter(s)
        # cnt = 0
        # seen_true = set()
        # seen_false = set()
        # for w in words:
        #     if w in seen_true:
        #         cnt += 1
        #     elif w in seen_false:
        #         pass
        #     else:
        #         if is_subsequence(w):
        #             seen_true.add(w)
        #             cnt += 1
        #         else:
        #             seen_false.add(w)
        # return cnt
