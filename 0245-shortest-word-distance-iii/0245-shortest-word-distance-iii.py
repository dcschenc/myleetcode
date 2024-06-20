class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # index1, index2 = float('-inf'), float('-inf')
        # min_distance = float('inf')
        # for i, word in enumerate(wordsDict):
        #     if word == word1:
        #         if word1 == word2:
        #             index1, index2 = index2, i
        #         else:
        #             index1 = i
        #     elif word == word2:
        #         index2 = i

        #     if index1 != float('-inf') and index2 != float('-inf'):
        #         min_distance = min(min_distance, abs(index1 - index2))

        # return min_distance

        hm = defaultdict(list)
        for i in range(len(wordsDict)):
            hm[wordsDict[i]].append(i)
        word1_list = hm[word1]
        word2_list = hm[word2]

        dist = float('inf')
        if word1 == word2:
            for i in range(1, len(word1_list)):
                dist = min(dist, word1_list[i] - word1_list[i-1])
        else:
            i, j = 0, 0
            while i < len(word1_list) and j < len(word2_list):
                dist = min(dist, abs(word1_list[i] - word2_list[j]))
                if word1_list[i] < word2_list[j]:
                    i += 1
                else:
                    j += 1
        return dist