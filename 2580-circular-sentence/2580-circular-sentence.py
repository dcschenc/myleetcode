class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        for i, w in enumerate(words[1:]):
            if w[0] != words[i][-1]:
                return False
        return words[0][0] == words[-1][-1]