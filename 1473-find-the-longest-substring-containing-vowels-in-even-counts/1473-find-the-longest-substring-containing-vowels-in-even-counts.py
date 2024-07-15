from collections import defaultdict
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Initialize a list to store the first position we encounter a given state
        # State is represented as a bitmask integer of size 32 (for 5 vowels, each can be on/off)
        positions = [inf] * 32

        # The starting state (all vowels have even counts) is at index 0
        positions[0] = -1

        # List of vowels for reference
        vowels = 'aeiou'

        # `state` to keep track of the count of vowels encountered (even/odd as a bitmask)
        # `max_length` to keep track of the length of the longest valid substring so far
        state = max_length = 0

        # Iterate over the string characters with their index
        for index, char in enumerate(s):
            # Check if the current character is a vowel
            for j, vowel in enumerate(vowels):
                # Toggle the corresponding bit if we encounter a vowel
                if char == vowel:
                    state ^= 1 << j

            # Calculate max length using current index and first index where current state was seen
            max_length = max(max_length, index - positions[state])
            # Update the position for this state if it's the first time we're seeing this state
            positions[state] = min(positions[state], index)

        return max_length

        
            
        # ans = 0
        # hm = defaultdict(list)
        # for i in range(len(s)):
        #     if s[i] in 'aeiou':
        #         hm[s[i]].append(i)
        #     left = 0
        #     for c in 'aeiou':
        #         idxs = hm[c]
        #         # if len(idxs) == 1:
        #         #     left = max(left, idxs[0] + 1)
        #         if len(idxs)%2 != 0:
        #             left = max(left, idxs[0] + 1)
        #     ans = max(ans, i-left+1)
        # return ans