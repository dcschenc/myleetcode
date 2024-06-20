from collections import defaultdict
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # index1, index2 = float('-inf'), float('-inf')
        # min_distance = float('inf')

        # for i, word in enumerate(wordsDict):
        #     if word == word1:
        #         index1 = i
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
        for i in word1_list:
            for j in word2_list:
                dist = min(dist, abs(i-j))
        return dist