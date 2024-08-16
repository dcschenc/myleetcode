# class Solution:
#     def countPrefixSuffixPairs(self, words: List[str]) -> int:
#         total = 0
#         n = len(words)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if words[j].startswith(words[i]) and words[j].endswith(words[i]):
#                     total += 1
#         return total

# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/solutions/4745155/python-solution-prefix-and-suffix-tries-optimized-solution/
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str, reverse = False) -> Set[str]:
        curChars, indices = self.root, set()
        for char in word:
            if char in curChars:
                curChars = curChars[char]
            else:
                curChars[char] = {}
                curChars = curChars[char]
            if 'end' in curChars:
                indices.add(curChars['end'])
        curChars['end'] = word if not reverse else word[::-1]
        return indices

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefix, suffix = Trie(), Trie()
        count, res = defaultdict(int), 0
        for word in words:
            indicesPrefix = prefix.insert(word)
            indicesSuffix = suffix.insert(word[::-1], True)
            for chars in indicesPrefix:
                if chars in indicesSuffix:
                    res += count[chars]
            count[word] += 1
        return res
       