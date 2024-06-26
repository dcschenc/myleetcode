class TrieNode:
    def __init__(self):
        self.children = [None] * 128  # All ASCII characters
        self.is_end_of_word = False  # Flag to mark the end of a word

    def insert(self, word: str) -> None:
        # Insert a word into the trie
        node = self
        for char in word:
            index = ord(char)  # Get ASCII value for the character
            if node.children[index] is None:
                node.children[index] = TrieNode()  # Create a new node if necessary
            node = node.children[index]
        node.is_end_of_word = True  # Mark the end of the word

class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # Initialize the Trie and insert all the words
        trie = TrieNode()
        for word in words:
            trie.insert(word)

        n = len(s)
        pairs = []  # To hold start and end indexes of bold areas

        # Find all occurrences of words in 's'
        for start in range(n):
            node = trie
            for end in range(start, n):
                index = ord(s[end])
                if node.children[index] is None:
                    break
                node = node.children[index]
                if node.is_end_of_word:
                    pairs.append([start, end])

        # If no matches are found, return the original string
        if not pairs:
            return s

        # Merge the overlapping intervals
        merged_intervals = []
        start, end = pairs[0]
        for interval_start, interval_end in pairs[1:]:
            if end + 1 < interval_start:
                merged_intervals.append([start, end])
                start, end = interval_start, interval_end
            else:
                end = max(end, interval_end)
        merged_intervals.append([start, end])

        # Build the final string with bold tags
        answer = []
        index = 0
        for start, end in merged_intervals:
            # Add non-bold part of string
            if index < start:
                answer.append(s[index:start])
            # Add the bold tag and the bold part of string
            answer.append('<b>' + s[start:end + 1] + '</b>')
            # Update the index to the end of the bold part
            index = end + 1

        # Add any remaining non-bold part of the string
        if index < n:
            answer.append(s[index:])

        # Join all parts to form the final string
        return ''.join(answer)