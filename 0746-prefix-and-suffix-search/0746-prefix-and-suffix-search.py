class TrieNode:
    def __init__(self):
        # Initialize the children to be a list of 26 elements for each letter in the alphabet
        self.children = [None] * 26
        # Initialize an empty list to hold the indexes at which the words appear
        self.indexes = []

    def insert(self, word, index):
        node = self
        for char in word:
            char_index = ord(char) - ord('a')  # Find the index of the character
            if node.children[char_index] is None:
                node.children[char_index] = TrieNode()  # Create a TrieNode if it doesn't exist
            node = node.children[char_index]
            node.indexes.append(index)  # Appends index to indexes list at each node along the path

    def search(self, prefix):
        node = self
        for char in prefix:
            char_index = ord(char) - ord('a')  # Convert char to index
            if node.children[char_index] is None:
                return []  # Return empty list if character path doesn’t exist
            node = node.children[char_index]
        return node.indexes  # Return the indexes list if the prefix is found


class WordFilter:
    def __init__(self, words):
        self.prefix_trie = TrieNode()  # Trie to store the prefixes
        self.suffix_trie = TrieNode()  # Trie to store the reverse of the suffixes for easier matching
        for index, word in enumerate(words):
            self.prefix_trie.insert(word, index)
            # Insert reversed word into suffix trie to handle suffix searches
            self.suffix_trie.insert(word[::-1], index)

    def f(self, prefix, suffix):
        prefix_indexes = self.prefix_trie.search(prefix)
        suffix_indexes = self.suffix_trie.search(suffix[::-1])  # Reverse suffix to match with our suffix trie
        if not prefix_indexes or not suffix_indexes:
            return -1
      
        # Use two pointers to find the largest index which is common in both prefix and suffix indexes lists
        i, j = len(prefix_indexes) - 1, len(suffix_indexes) - 1
        while i >= 0 and j >= 0:
            if prefix_indexes[i] == suffix_indexes[j]:
                return prefix_indexes[i]
            if prefix_indexes[i] > suffix_indexes[j]:
                i -= 1
            else:
                j -= 1
        return -1  # Return -1 if no common index is found


# The WordFilter object will be instantiated and called as such:
# word_filter = WordFilter(words)
# result = word_filter.f(prefix, suffix)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)