class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        def find_root(x):
            if root[x] == x:
                return x
            root[x] = find_root(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find_root(x)
            rootY = find_root(y)
            if rootX != rootY:
                root[rootY] = rootX

        if len(sentence1) != len(sentence2):
            return False
        words = []
        for w1, w2 in similarPairs:
            if w1 not in words:
                words.append(w1)
            if w2 not in words:
                words.append(w2)

        root = {w:w for w in words}
       
        for w1, w2 in similarPairs:
            union(w1, w2)

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 == w2:
                continue
            if w1 in words and w2 in words and find_root(w1) == find_root(w2):
                continue
           
            return False
        return True