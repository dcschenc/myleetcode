class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.value = -1        

class FileSystem:
    def __init__(self):
        self.root = TrieNode()        

    def createPath(self, path: str, value: int) -> bool:
        cur = self.root
        words = path.split('/')[1:]
        n = len(words)
        for i, w in enumerate(words):
            if w not in cur.children:
                if n - 1 != i:
                    return False
                cur.children[w] = TrieNode()                
            cur = cur.children[w]
        if cur.is_end:
            return False
        cur.is_end = True
        cur.value = value
        return True

    def get(self, path: str) -> int:
        cur = self.root
        words = path.split('/')[1:]
        for w in words:
            if w not in cur.children:
                return -1
            cur = cur.children[w]
        return cur.value


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)