class TrieNode:
    def __init__(self):
        self.children = {}
        self.sentences = defaultdict(int)  # store the sentences

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        for sentence, count in zip(sentences, times):
            self.add_to_trie(sentence, count)
            
        self.cur = []  # current characters
        self.curr_node = self.root
        self.dead = TrieNode()

    def add_to_trie(self, sentence, count):
        node = self.root
        for c in sentence:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.sentences[sentence] += count
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.cur)
            self.add_to_trie(curr_sentence, 1)
            self.curr_sentence = []
            self.curr_node = self.root
            return []
        
        self.cur.append(c)
        if c not in self.curr_node.children:
            self.curr_node = self.dead
            return []
        
        self.curr_node = self.curr_node.children[c]
        sentences = self.curr_node.sentences
        sorted_sentences = sorted(sentences.items(), key = lambda x: (-x[1], x[0]))
        
        ans = []
        for i in range(min(3, len(sorted_sentences))):
            ans.append(sorted_sentences[i][0])
        
        return ans

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.times = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence, time):
        cur = self.root
        for c in sentence:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        cur.times += time

class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.trie = Trie()
        self.cur = self.trie.root
        self.dead = False
        self.prefix = ''
        for sentence, time in zip(sentences, times):
            self.trie.insert(sentence, time)              

    def input(self, c: str) -> List[str]:
        def dfs(node, cur):         
            if node.is_end:
                res.append((self.prefix + ''.join(cur), node.times))
            for k, child in node.children.items():
                dfs(child, cur + [k])

        if c == '#':
            self.cur = self.trie.root            
            self.trie.insert(self.prefix, 1)
            self.prefix = ''
            self.dead = False
            return []

        self.prefix += c
        if c not in self.cur.children or self.dead:
            self.dead = True
            return []
        self.cur = self.cur.children[c]        
        res = []
        dfs(self.cur, [])
        res.sort(key=lambda x: (-x[1], x[0]))
        return [x[0] for x in res[:3]]          
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)