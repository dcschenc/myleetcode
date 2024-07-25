class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1813.Sentence%20Similarity%20III
        words1, words2 = sentence1.split(), sentence2.split()
        m, n = len(words1), len(words2)
        if m < n:
            words1, words2 = words2, words1
            m, n = n, m
        i = j = 0
        while i < n and words1[i] == words2[i]:
            i += 1
        while j < n and words1[m - 1 - j] == words2[n - 1 - j]:
            j += 1
        return i + j >= n


        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) < len(words2):
            words1, words2 = words2, words1
        j, n = 0, len(words2)
        i, m = 0, len(words1)
        while j < n:
            if words1[i] == words2[j]  :
                i += 1
                j += 1
            else:
                break
        if j < n:
            return words2[j:] == words1[m-(n-j):]
        else:
            return True