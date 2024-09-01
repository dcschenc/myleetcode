class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.words.append(word)
    
    def find_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.words


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def backtrack(step, word_square):
            if step == n:
                results.append(word_square[:])
                return
            
            prefix = ''.join([word_square[i][step] for i in range(step)])
            for candidate in trie.find_words_with_prefix(prefix):
                word_square.append(candidate)
                backtrack(step + 1, word_square)
                word_square.pop()
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        n = len(words[0])
        results = []
        for word in words:
            word_square = [word]
            backtrack(1, word_square)
        
        return results
