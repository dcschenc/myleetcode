from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1, counter2 = Counter(words1), Counter(words2)
        set1 = set([word for word in counter1 if counter1[word] == 1])
        set2 = set([word for word in counter2 if counter2[word] == 1])
        return len(set1 & set2)
