from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        for c in string.ascii_lowercase:
            if abs(counter1[c] - counter2[c]) > 3:
                return False
        return True