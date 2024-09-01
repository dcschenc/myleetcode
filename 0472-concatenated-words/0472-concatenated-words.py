class Trie:
    def __init__(self):
        self.children = [None] * 26  
        self.is_end_of_word = False   

    def insert(self, word):
        node = self
        for char in word:
            index = ord(char) - ord('a')            
            if node.children[index] is None:
                node.children[index] = Trie()            
            node = node.children[index]        
        node.is_end_of_word = True

class Solution:   
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0472.Concatenated%20Words
        def dfs(word):
            if not word: 
                return True
            node = trie  
            for i, char in enumerate(word):
                index = ord(char) - ord('a')
                # If the character is not in the trie, the word cannot be formed
                if node.children[index] is None:
                    return False
                node = node.children[index]
                # If the current node is an end of a word and the next substring is also a word
                if node.is_end_of_word and dfs(word[i + 1:]):
                    return True  
            return False  
            
        trie = Trie()
        concatenated_words = []
        words.sort(key=len)
        for word in words:
            if dfs(word):
                concatenated_words.append(word)
            else:
                trie.insert(word)
        return concatenated_words
