class WordDistance:
    def __init__(self, wordsDict: List[str]):
        # self.wordsDict = wordsDict
        self.hm = defaultdict(list)
        for i in range(len(wordsDict)):
            self.hm[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        word_idx1, word_idx2 = self.hm[word1], self.hm[word2]
        dist = float('inf')
        # for i in word1_idx:
        #     for j in word2_idx:
        #         dist = min(dist, abs(i-j))
        i = j = 0
        while i < len(word_idx1) and j < len(word_idx2):
            dist = min(dist, abs(word_idx1[i] - word_idx2[j]))
            if word_idx1[i] <= word_idx2[j]:
                i += 1
            else:
                j += 1
        return dist


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)